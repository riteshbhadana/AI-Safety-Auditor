# agent/safety_agent.py

def run_safety_agent(violation, ai_analysis):
    if violation["severity"] == "HIGH":
        return {
            "action": "GENERATE_REPORT",
            "analysis": ai_analysis
        }
    return {"action": "IGNORE"}
