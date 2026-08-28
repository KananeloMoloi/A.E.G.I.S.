from ai.ollama import OllamaAI
from agents.manager import AgentManager


def main():

    print("="*60)
    print("                 A.E.G.I.S")
    print("="*60)

    print("AI ENGINE : Ollama")
    print("MODEL     :qwen3:4b")
    print("AGENTS    :ONLINE")
    print("STATUS    :ONLINE")

    print("="*60)
    ai = OllamaAI()

    manager = AgentManager(ai)

    while True:

        user_input = input("\n YOU:")

        if user_input.lower()== "exit":
            print("\n A.E.G.I.S : shutting down")
            break
        if not user_input.strip():
            continue

        try:

            answer = manager.run(user_input)

            print("\nA.E.G.I.S :")
            print(answer)

        except Exception as error:

            print("\nSYSTEM ERROR:")
            print(error)

if __name__ == "__main__":
    main()