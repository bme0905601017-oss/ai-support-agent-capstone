# Final Capstone — Ola Domain Support Agent (CrewAI)

**Track:** Business Operations / Customer Support (Ola)  
**Status:** Completed under `MOCK_LLM` with zero API keys and zero network access.  
**Telemetry Disabled:** `CREWAI_DISABLE_TELEMETRY=true` and `OTEL_SDK_DISABLED=true` enforced.

---

## Dataset Design Choices (Part 1, Task 1)
- **Seed:** `42`
- **Total Records:** `45` support tickets (≥40 required)
- **Categories Used:** `Billing`, `Technical Issue`, `Account Access`, `Product Defect`, `General Inquiry` (every category used at least 3 times).
- **Statuses Used:** `Open`, `In Progress`, `Escalated`, `Resolved`, `Closed` (every status used at least once).
- **Resolution Time Range:** 2 to 72 hours (chosen to reflect realistic ticket lifecycles for quick-commerce / ride-hailing support operations).
- **Escalated Percentage:** ~22% (landing cleanly within the required 10% to 30% band).

---

## RAG Core & Threshold Calibration (Part 1, Tasks 3–5)
- **Chunking Strategies Implemented:** Fixed-size with overlap vs. Sentence-based chunks.
- **Embedding Model:** Local `SentenceTransformers` model (`all-MiniLM-L6-v2`).
- **Vector Index:** Separate ChromaDB collections (`ola_fixed_chunks`, `ola_sentence_chunks`).
- **Empirical Threshold Calibration:** Measured top-1 cosine similarity across 3 in-scope queries (avg ~0.78) and 2 out-of-scope queries (avg ~0.34). Threshold set empirically at **`0.55`** to cleanly separate in-scope retrieval from out-of-scope fallback ("I don't know").

---

## Architecture & Governance Summary
- **Part 2:** CrewAI Multi-Agent Orchestration (Retrieval Agent, Lookup Agent, Response Composer), in-process chat memory, Pydantic structured outputs, and input/output guardrails.
- **Part 3:** FastAPI backend with `/ask`, `/add-document`, and a resilient WebSocket chat endpoint (`@app.websocket`), plus ELK-style JSON-Lines logging with PII scrubbing.
- **Part 4:** Autogen 2-agent Round Robin review stage (`max_turns=2`), least-autonomy tool restriction, runtime token/cost budget cap, and in-memory response caching.
