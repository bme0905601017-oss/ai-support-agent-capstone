import pytest
from dataset import SUPPORT_TICKETS
from src.pii_scrubber import scrub_pii
from src.rule_checker import check_budget_cap, verify_least_autonomy
from src.agents.resolution_agent import check_support_ticket_status

def test_dataset_generation():
    assert len(SUPPORT_TICKETS) >= 40

def test_pii_scrubbing():
    sample = "Call me at 9876543210 regarding my ride."
    scrubbed = scrub_pii(sample)
    assert "9876543210" not in scrubbed
    assert "[REDACTED_PHONE]" in scrubbed

def test_budget_cap():
    assert check_budget_cap(150, 500) == True
    with pytest.raises(ValueError):
        check_budget_cap(600, 500)

def test_least_autonomy():
    assert verify_least_autonomy("Ticket Lookup Specialist", "check_support_ticket_status") == True
    assert verify_least_autonomy("Retrieval Specialist", "check_support_ticket_status") == False

def test_ticket_lookup():
    sample_id = SUPPORT_TICKETS[0]["record_id"]
    res = check_support_ticket_status(sample_id)
    assert "status" in res
    assert "escalation_score" in res
