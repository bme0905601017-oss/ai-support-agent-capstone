ai-support-agent-capstone/
│
├── data/
│   ├── sample_tickets.json        # Simulated customer queries/tickets
│   └── knowledge_base.json        # Sample policy / FAQ documents
│
├── src/
│   ├── agents/
│   │   ├── intake_agent.py        # Validates order/ticket details
│   │   ├── risk_agent.py          # Flags anomalies, PII, high values
│   │   └── resolution_agent.py    # Formulates policy answers & refunds
│   ├── guards/
│   │   ├── pii_scrubber.py        # Local PII redaction (Regex / Presidio)
│   │   └── rule_checker.py        # Confidential rule disclosure checks
│   └── main.py                    # Multi-agent orchestrator entry point
│
├── tests/
│   └── test_agents.py             # Unit tests for agent functions
│
├── .gitignore
├── requirements.txt               # Dependencies (e.g., langchain, pydantic)
└── README.md                      # Comprehensive project documentation
