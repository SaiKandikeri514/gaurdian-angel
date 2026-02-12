# 🛡️ Guardian Angel - AI-Powered Security Code Review Agent

**Guardian Angel** is an intelligent AI agent that automates security code reviews for developers. Built using Google's Gemini 2.0 Flash model, it leverages a multi-agent architecture to detect vulnerabilities and propose secure fixes in real-time.

---

## ✨ Features

- **🔍 Automated Vulnerability Detection**: Scans code for security flaws including:
  - Hardcoded credentials
  - SQL injection vulnerabilities
  - XSS (Cross-Site Scripting)
  - SAP BTP-specific security issues (XSUAA, CAP, Cloud SDK)
  - And more...

- **🛡️ Secure Code Generation**: Automatically generates secure fixes with strict "Do No Harm" guardrails to preserve business logic

- **📊 Human-Readable Reports**: Clear, formatted security analysis with:
  - Risk scores with detailed justification
  - Severity indicators (🔴 High, 🟠 Medium, 🔵 Low)
  - Line-by-line vulnerability explanations
  - Executive summaries

- **🎨 Modern UI**: Interactive Streamlit dashboard with:
  - Clean, formatted security reports
  - Side-by-side code comparison
  - Detailed diff view
  - Accept/Reject workflow

- **🤖 Multi-Agent Architecture**: Orchestrator-Worker pattern with specialized agents:
  - `SecurityOrchestrator`: Manages workflow
  - `VulnerabilityScanner`: Detects security issues
  - `SecureRefactorer`: Generates fixes

---

## 🏗️ Architecture

```
User → Streamlit UI → SecurityOrchestrator
                           ↓
        ┌──────────────────┴────────────────────┐
        ↓                                       ↓
VulnerabilityScanner                  SecureRefactorer
        ↓                                       ↓
   Gemini 2.0 Flash                      Gemini 2.0 Flash
        ↓                                       ↓
  Human-Readable Report                  Secure Code
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Google AI Studio API Key ([Get it here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd sap-security-agent
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📖 Usage

1. **Paste Your Code**: Copy and paste your code snippet into the text area
2. **Click "Analyze & Fix"**: The agent will scan for vulnerabilities
3. **Review Results**: 
   - Read the formatted security analysis report
   - Check risk scores and vulnerability details
   - View the proposed secure code fix
   - Compare the original vs. fixed code
4. **Accept or Reject**: Choose to apply or discard the fix

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **AI Model** | Google Gemini 2.0 Flash |
| **Frontend** | Streamlit |
| **Backend** | Python 3.12 |
| **Agent Framework** | Custom Multi-Agent Architecture |
| **Libraries** | `google-generativeai`, `python-dotenv` |

---

## 📁 Project Structure

```
sap-security-agent/
├── agent.py              # Multi-agent implementation
├── app.py                # Streamlit UI application
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── verify_agent.py       # Verification scripts
├── verify_guardrails.py  # Guardrail tests
└── README.md             # This file
```

---

## 🧪 Testing

Test the multi-agent architecture:
```bash
python verify_multi_agent.py
```

Test safety guardrails:
```bash
python verify_guardrails.py
```

---

## 🎯 Key Innovations

- **Human-Readable Output**: Clear, formatted reports instead of raw JSON for better developer experience
- **SAP BTP Awareness**: Specialized prompts for SAP-specific vulnerabilities
- **Chain of Thought**: Agent explains *why* vulnerabilities exist with detailed descriptions
- **Guardrails**: "Do No Harm" policy preserves business logic during refactoring
- **Multi-Agent Architecture**: Specialized agents for scanning and refactoring ensure focused, high-quality results

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 💡 Acknowledgments

- Built with [Google Gemini](https://ai.google.dev/)
- Powered by [Streamlit](https://streamlit.io/)

---

**Built for hackathon excellence** 🏆
