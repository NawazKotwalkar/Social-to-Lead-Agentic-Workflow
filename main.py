from dotenv import load_dotenv
load_dotenv()
from graph import build_graph
from state import AgentState

def main():
    app = build_graph()

    state: AgentState = {
        "intent": None,
        "name": None,
        "email": None,
        "platform": None,
        "last_user_message": None,
        "response": ""
    }

    print("AutoStream Agent is live. Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        if "@" in user_input:
            state["email"] = user_input
        elif state["intent"] == "high_intent" and not state["name"]:
            state["name"] = user_input
        elif state["intent"] == "high_intent" and state["name"] and not state["platform"]:
            state["platform"] = user_input

        state["last_user_message"] = user_input
        state = app.invoke(state)

        print("Agent:", state["response"])

if __name__ == "__main__":
    main()
