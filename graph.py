# graph.py
from llm import generate_answer
from langgraph.graph import StateGraph, END
from state import AgentState
from intent import classify_intent
from rag import answer_with_rag
from tools import mock_lead_capture


def intent_node(state: AgentState):
    message = state["last_user_message"]
    if state.get("intent") == "high_intent":
        return state
    state["intent"] = classify_intent(message)
    return state



def response_node(state: AgentState):
    intent = state["intent"]
    message = state["last_user_message"]

    if intent == "greeting":
        state["response"] = "Hi! I can help you with AutoStream pricing and plans."
        return state

    if intent == "inquiry":
        context = answer_with_rag(message)
        state["response"] = generate_answer(context, message)
        return state

    if intent == "high_intent":
        missing = []
        if not state.get("name"):
            missing.append("name")
        if not state.get("email"):
            missing.append("email")
        if not state.get("platform"):
            missing.append("platform")

        if missing:
            state["response"] = f"To get you started, I need your {missing[0]}."
            return state

        mock_lead_capture(
            state["name"],
            state["email"],
            state["platform"]
        )
        state["response"] = "You’re all set! We’ve successfully captured your details."
        return state

    # 🔐 Fallback (never let response be missing)
    state["response"] = "I can help you with pricing, plans, or getting started."
    return state


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("intent", intent_node)
    graph.add_node("response", response_node)

    graph.set_entry_point("intent")
    graph.add_edge("intent", "response")
    graph.add_edge("response", END)

    return graph.compile()