from agent import SecurityAgent
import sys

def log(message):
    print(message)
    with open("verification_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

def test_hardcoded_credentials():
    with open("verification_log.txt", "w", encoding="utf-8") as f:
        f.write("Starting Verification...\n")
        
    log("Testing Hardcoded Credentials...")
    code = """
def connect_db():
    conn = connect("user='admin', password='password123'")
"""
    agent = SecurityAgent()
    analysis = agent.analyze_code(code)
    log(f"Analysis:\n{analysis}")
    
    if "Hardcoded credentials" in analysis or "Password" in analysis or "credentials" in analysis.lower():
        log("✅ Detected Hardcoded Credentials")
    else:
        log("❌ Failed to detect Hardcoded Credentials")

    fixed = agent.fix_code(code, analysis)
    log(f"Fixed Code:\n{fixed}")
    if "os.getenv" in fixed or "os.environ" in fixed:
        log("✅ Fix uses environment variables")
    else:
        log("❌ Fix might not be optimal")

if __name__ == "__main__":
    try:
        test_hardcoded_credentials()
    except Exception as e:
        log(f"Test Failed: {e}")
        sys.exit(1)
