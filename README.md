# Social to Lead Agentic Workflow


## 1. How to Run the Project Locally

### Prerequisites

* Python 3.9 or higher
* A free Gemini API key from Google AI Studio

### Steps

1. Clone the repository and navigate into the project directory:

git clone <your-repository-url>
cd autostream-agent

2. Install the required dependencies:

pip install -r requirements.txt

3. Create a `.env` file in the project root directory and add your API key:

GEMINI_API_KEY=your_api_key_here

4. Run the agent:

python main.py

The agent will start in the terminal and support multi-turn conversations.
Type `exit` to stop the program.


## 2. Architecture Explanation

This project implements a **stateful conversational AI agent** using **LangGraph**, which was chosen to explicitly model the agent’s workflow as a graph of deterministic steps. LangGraph enables controlled state transitions and prevents unsafe or premature tool execution.

The agent maintains a structured state object that persists across multiple conversation turns. This state stores detected intent and user-provided details such as name, email, and creator platform, allowing the agent to retain memory over 5–6 or more turns.

For informational queries, the agent uses a **Retrieval-Augmented Generation (RAG)** pipeline. Pricing and policy data are stored locally and embedded using SentenceTransformers, with FAISS used for similarity-based retrieval. The retrieved context is passed to the Gemini 1.5 Flash LLM, which generates grounded responses strictly based on the retrieved information.

Backend actions are implemented as explicit tools. The lead capture tool is gated by state checks and is triggered only after all required user details are collected, ensuring safe and correct execution. This separation of reasoning, memory, and side effects reflects real-world agent system design.

---

## 3. WhatsApp Deployment – Webhook Integration

To deploy this agent on WhatsApp, it can be integrated using the **WhatsApp Business API** through webhooks. Incoming WhatsApp messages would be received by a backend server (e.g., built with FastAPI or Flask) and forwarded to the agent for processing.

The agent’s response would then be sent back to the user via the WhatsApp API. To maintain conversation continuity, the agent state can be stored in an external database or Redis instance, keyed by the user’s phone number. This allows the agent to retain memory across messages and sessions while operating at scale.

This webhook-based architecture enables real-time, stateful interactions on WhatsApp while preserving safe tool execution and controlled agent behavior.