from agent import SecurityAgent
import json

def test_json_output():
    print("Testing JSON Output and SAP Context...")
    code = """
# SAP CAP Service
def srv(req):
    # Hardcoded credentials for XSUAA
    xsuaa_creds = {
        "clientid": "sb-clone",
        "clientsecret": "hardcoded_secret"
    }
    return "Hello"
"""
    agent = SecurityAgent()
    analysis_json = agent.analyze_code(code)
    print(f"Raw Output:\n{analysis_json}\n")
    
    try:
        data = json.loads(analysis_json)
        print("✅ JSON Parsed Successfully")
        print(f"Risk Score: {data.get('risk_score')}")
        
        vulnerabilities = data.get('vulnerabilities', [])
        if any("credential" in v['type'].lower() or "hardcoded" in v['type'].lower() for v in vulnerabilities):
             print("✅ Detected Credential Issue")
        else:
             print("❌ Failed to detect credential issue")
             
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")

if __name__ == "__main__":
    test_json_output()
