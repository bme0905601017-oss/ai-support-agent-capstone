def verify_least_autonomy(agent_name: str, tool_name: str) -> bool:
    """Enforces principle of least autonomy: only Lookup Agent can call ticket status."""
    if tool_name == "check_support_ticket_status" and agent_name != "Ticket Lookup Specialist":
        return False
    return True

def check_budget_cap(tokens_requested: int, max_budget: int = 500) -> bool:
    """Enforces runtime cost/token budget cap."""
    if tokens_requested > max_budget:
        raise ValueError(f"Runtime budget cap exceeded: Requested {tokens_requested} tokens exceeds maximum budget of {max_budget}.")
    return True
