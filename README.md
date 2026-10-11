# Customer Support AI Agent Capstone Project

**Domain:** Support  
**Project Overview:** An end-to-end multi-agent AI system designed to handle high-volume customer support tickets, automate routine resolutions, detect anomalies/PII leaks, and maintain human-in-the-loop escalation paths.

---

## Key Features

1. **Intake & Validation Agent:** Parses incoming customer tickets and verifies order/policy IDs.
2. **Risk & Guardrail Engine:** Scans outputs for PII leaks and confidential policy rules using open-source guardrails.
3. **Automated Resolution Agent:** Resolves routine refund or policy queries deterministically.
4. **Human-in-the-Loop Escalation:** Automatically routes high-value or ambiguous tickets to human review.

---

## Repository Structure

- `src/agents/`: Core LLM agents and multi-agent coordination logic.
- `src/guards/`: Output sanitization routines for PII and confidential data protection.
- `data/`: Mock datasets representing tickets and knowledge base articles.

---

## Setup & Running

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
