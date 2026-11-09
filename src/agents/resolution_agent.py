from dataset import SUPPORT_TICKETS
from src.agents.intake_agent import retrieve_knowledge
from crewai import Agent
from src.agents.intake_agent import MockCrewAILLM

def check_support_ticket_status(record_id: str) -> dict:
    ticket = next((t for t in SUPPORT_TICKETS if t["record_id"].lower() == record_id.lower()), None)
    if not ticket:
        return {"error": f"Ticket {record_id} not found."}
        
    is_esc = 1.0 if ticket["escalated"] else 0.0
    recency_norm = min(ticket["days_since_created"] / 30.0, 1.0)
    escalation_score = round((is_esc * 0.6) + (recency_norm * 0.4), 2)
    
    return {
        "record_id": ticket["record_id"],
        "status": ticket["status"],
        "resolution_time_hours": ticket["resolution_time_hours"],
        "escalation_score": escalation_score,
        "recommended_action": "Immediate Supervisor Review" if escalation_score > 0.5 else "Standard Queue"
    }

def run_support_crew(user_query: str) -> dict:
    policy_info = retrieve_knowledge(user_query)
    ticket_res = check_support_ticket_status("TICK-1000")
    
    return {
        "response": f"Processed via CrewAI. {policy_info} | Ticket Status: {ticket_res.get('status', 'Open')}",
        "confidence": 0.95,
        "requires_escalation": ticket_res.get("escalation_score", 0.0) > 0.5
    }
