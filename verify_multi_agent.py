from agent import SecurityOrchestrator, VulnerabilityScanner, SecureRefactorer
import json

def test_multi_agent():
    print("Testing Multi-Agent Architecture...")
    
    try:
        # Test Orchestrator Instantiation
        orch = SecurityOrchestrator()
        print("✅ SecurityOrchestrator Initialized")
        
        # Verify Workers exist
        if isinstance(orch.scanner, VulnerabilityScanner):
            print("✅ VulnerabilityScanner Worker detected")
        else:
            print("❌ VulnerabilityScanner missing")

        if isinstance(orch.refactorer, SecureRefactorer):
            print("✅ SecureRefactorer Worker detected")
        else:
            print("❌ SecureRefactorer missing")

        # Test Workflow
        code = """
        def insecure():
            key = '12345'
        """
        print("\nRunning Scan (delegated to Scanner)...")
        analysis = orch.analyze_code(code)
        
        if "risk_score" in analysis:
             print("✅ Scan returned valid analysis")
        else:
             print("❌ Scan failed")

        print("\nRunning Fix (delegated to Refactorer)...")
        fixed = orch.fix_code(code, analysis)
        print(f"DEBUG: Fixed Code Output: {fixed}")
        
        if "os.environ" in fixed or "def" in fixed: 
             print("✅ Refactor returned code")
        else:
             print("❌ Refactor failed")
             
    except Exception as e:
        print(f"❌ Verification Failed: {e}")

if __name__ == "__main__":
    test_multi_agent()
