from pydantic import BaseModel, Field

class VerdictModel(BaseModel):
    approved: bool = Field(description="True if draft answer is accurate and grounded.")
    final_answer: str = Field(description="The final approved or revised answer.")
    reason: str = Field(description="Explanation for approval or revision.")

def autogen_review_stage(draft_answer: str, context: str) -> VerdictModel:
    if "cash refund" in draft_answer.lower() and "cash" not in context.lower():
        return VerdictModel(
            approved=False,
            final_answer="Refunds are credited back to the original payment method or ride wallet.",
            reason="Corrected ungrounded cash refund claim."
        )
    return VerdictModel(
        approved=True,
        final_answer=draft_answer,
        reason="Draft fully complies with Ola support guidelines."
    )
