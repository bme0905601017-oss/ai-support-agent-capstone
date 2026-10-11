import random

def generate_support_tickets(seed=42, num_records=45):
    random.seed(seed)
    categories = ["Billing", "Technical Issue", "Account Access", "Product Defect", "General Inquiry"]
    statuses = ["Open", "In Progress", "Escalated", "Resolved", "Closed"]
    
    # Ensure every category and status is used at least once
    support_tickets = []
    
    for i in range(num_records):
        record_id = f"TICK-{1000 + i}"
        # Force baseline coverage for first 5 items, then random
        category = categories[i] if i < len(categories) else random.choice(categories)
        status = statuses[i % len(statuses)]
        
        # Realistic resolution time: 2 to 72 hours
        resolution_time_hours = round(random.uniform(2.0, 72.0), 1)
        days_since_created = random.randint(0, 30)
        
        # Target ~20-25% escalation rate
        escalated = random.choices([True, False], weights=[0.22, 0.78])[0]
        
        ticket = {
            "record_id": record_id,
            "category": category,
            "status": status,
            "resolution_time_hours": resolution_time_hours,
            "days_since_created": days_since_created,
            "escalated": escalated
        }
        support_tickets.append(ticket)
        
    return support_tickets

if __name__ == "__main__":
    tickets = generate_support_tickets()
    print(f"Generated {len(tickets)} support tickets successfully.")
