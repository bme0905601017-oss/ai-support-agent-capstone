import os
import json
from crewai import Agent
from crewai.llms.base_llm import BaseLLM
from sentence_transformers import SentenceTransformer
import chromadb

# Disable telemetry globally to satisfy zero-network rules
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["OTEL_SDK_DISABLED"] = "true"

class MockCrewAILLM(BaseLLM):
    def __init__(self, model_name="mock-model"):
        super().__init__()
        self.model_name = model_name

    def call(self, messages, callbacks=None, **kwargs):
        prompt = str(messages).lower()
        if "status" in prompt or "lookup" in prompt:
            return "Thought: Looking up ticket.\nAction: check_support_ticket_status\nAction Input: {'record_id': 'TICK-1000'}"
        return "Thought: Querying KB.\nAction: rag_lookup\nAction Input: {'query': 'sla policy'}"

    def supports_stop_words(self) -> bool:
        return True

# Initialize local RAG core using knowledge_base.json
model = SentenceTransformer('all-MiniLM-L6-v2')
chroma_client = chromadb.Client()
kb_collection = chroma_client.get_or_create_collection(name="kb_collection")

try:
    with open("data/knowledge_base.json", "r") as f:
        kb_data = json.load(f).get("knowledge_base_documents", [])
    for doc in kb_data:
        kb_collection.upsert(
            ids=[doc["topic"]],
            embeddings=[model.encode(doc["content"]).tolist()],
            documents=[doc["content"]],
            metadatas=[{"topic": doc["topic"]}]
        )
except Exception:
    pass

def retrieve_knowledge(query: str) -> str:
    results = kb_collection.query(query_embeddings=[model.encode(query).tolist()], n_results=1)
    docs = results.get("documents", [[]])[0]
    distances = results.get("distances", [[0.0]])[0]
    if not docs or (distances and distances[0] > 0.85):
        return "I don't know based on the provided Ola support policies."
    return f"Based on Ola policies: {docs[0]}"

def create_intake_agent() -> Agent:
    return Agent(
        role="Retrieval Specialist",
        goal="Retrieve accurate knowledge base policy documents.",
        backstory="Expert in searching Ola policy documentation.",
        tools=[],
        llm=MockCrewAILLM(),
        verbose=True
    )
