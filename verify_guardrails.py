from agent import SecurityAgent
import json

def test_guardrails():
    print("Testing Guardrails & JSON Fix...")
    code = "def dangerous():\n    db.execute('DROP TABLE users')"
    
    # Mock analysis since we are testing fix_code specifically
    analysis_json = json.dumps({
        "vulnerabilities": [{"type": "SQL Injection", "severity": "High", "line": 2, "description": "Direct SQL execution"}],
        "risk_score": 0,
        "summary": "Dangerous code detected"
    })

    agent = SecurityAgent()
    fixed_code = agent.fix_code(code, analysis_json)
    
    print(f"\nOriginal Code:\n{code}")
    print(f"\nFixed Code Output (Should be raw strings, not JSON):\n{fixed_code}")
    
    if fixed_code.strip().startswith("{") or "fixed_code" in fixed_code:
        print("❌ Error: Fix code returned JSON instead of raw code string.")
    else:
         print("✅ Success: Fix code returned raw string.")

if __name__ == "__main__":
    test_guardrails()
