from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from pydantic import BaseModel
import uuid
from src.agents.resolution_agent import run_support_crew
from src.rule_checker import check_budget_cap
from src.pii_scrubber import scrub_pii

app = FastAPI(title="Ola Domain Support Agent API", version="1.0.0")

class AskRequest(BaseModel):
    query: str

class DocumentRequest(BaseModel):
    id: str
    topic: str
    content: str

@app.post("/ask")
def ask_support(req: AskRequest):
    trace_id = str(uuid.uuid4())
    try:
        check_budget_cap(200, 500)
        clean_query = scrub_pii(req.query)
        result = run_support_crew(clean_query)
        return {"trace_id": trace_id, "source": "crew", "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            clean_query = scrub_pii(data)
            response = run_support_crew(clean_query)
            await websocket.send_json(response)
    except WebSocketDisconnect:
        print("WebSocket client disconnected gracefully.")
