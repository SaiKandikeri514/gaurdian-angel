import streamlit as st
from agent import SecurityOrchestrator
import difflib
import json

st.set_page_config(page_title="Guardian Angel", layout="wide", page_icon="🛡️")

st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .stTextArea textarea {
        background-color: #262730;
        color: #ffffff;
    }
    .stTextArea textarea::placeholder {
        color: #ffffff;
        opacity: 0.7;
    }
    .stTextArea textarea:focus::placeholder {
        color: transparent;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 5px;
        height: 3em;
    }
    h1 {
        color: #ff4b4b;
    }
    .vuln-card {
        background-color: #ffffff;
        color: #333333;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .main-title {
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        color: #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# Logo and Title
col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    # st.image("assets/cross_me_logo.png", width=150) # Assuming logo is saved here, using placeholder for now
    st.markdown("<h1 class='main-title'>🛡️ Guardian Angel</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center'>
    <h3>🚀 Automate your code reviews.</h3>
    <p>Paste your code below. The agent will <strong>detect vulnerabilities</strong> and <strong>propose secure fixes</strong>.</p>
</div>
""", unsafe_allow_html=True)

# Initialize Orchestrator
if 'agent' not in st.session_state:
    try:
        st.session_state.agent = SecurityOrchestrator()
        st.toast("Security Orchestrator Ready", icon="🤖")
    except Exception as e:
        st.error(f"Error initializing orchestrator: {e}. Please check your .env file and API Key.")

# Input Section
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Simulated Pull Request")
    code_input = st.text_area("Paste code snippet here:", height=300, value="", placeholder="Enter your code here")

analyze_button = st.button("🔍 Analyze & Fix Vulnerabilities")

# ... (Previous code)

if analyze_button and code_input:
    if 'agent' in st.session_state:
        with st.spinner("🕵️‍♂️ Analyzing code for vulnerabilities..."):
            try:
                # 1. Analyze
                analysis_text = st.session_state.agent.analyze_code(code_input)
                
                # 2. Fix
                fixed_code = st.session_state.agent.fix_code(code_input, analysis_text)
                
                # Store results in session state
                st.session_state.analysis_text = analysis_text
                st.session_state.fixed_code = fixed_code
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")

# Results Section
if 'analysis_text' in st.session_state:
    st.divider()
    
    # Display the human-readable security report
    st.subheader("📋 Security Analysis Report")
    
    # Display the full analysis report in a nice container
    st.markdown(f"""
    <div style="
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #0068c9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    ">
        <div style="color: #333; line-height: 1.8; font-size: 1.05em;">
            {st.session_state.analysis_text.replace('**', '<strong>').replace('**', '</strong>').replace(chr(10), '<br/>')}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # Code Comparison
    st.subheader("✅ Secure Implementation")
    
    col_vuln, col_fix = st.columns(2)
    
    with col_vuln:
        st.markdown("### ❌ Vulnerable Code")
        st.code(code_input, language='python')
        
    with col_fix:
        st.markdown("### 🛡️ Fixed Code")
        st.code(st.session_state.fixed_code, language='python')

    # Diff View
    with st.expander("Show Detailed Diff"):
        diff = difflib.unified_diff(
            code_input.splitlines(),
            st.session_state.fixed_code.splitlines(),
            fromfile='Original',
            tofile='Fixed',
            lineterm=''
        )
        diff_text = "\n".join(list(diff))
        st.code(diff_text, language='diff')

    st.divider()
    st.subheader("🏁 Decision")
    
    col_accept, col_reject = st.columns(2)
    
    with col_accept:
        if st.button("✅ Accept Fix", key="btn_accept", help="Apply this fix to the codebase"):
            st.success("Fix accepted! Code has been updated (Simulated).")
            st.code(st.session_state.fixed_code, language='python')
            st.balloons()
            
    with col_reject:
        if st.button("❌ Reject Fix", key="btn_reject", help="Discard this fix"):
            st.warning("Fix rejected. You can modify the input code and analyze again.")
            # Optional: Clear state to force re-analysis if needed, but keeping it visible is often better for comparison.
