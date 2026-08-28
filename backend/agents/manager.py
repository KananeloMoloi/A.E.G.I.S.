from agents.chat import ChatAgent
from agents.research import ResearchAgent

class AgentManager:

    def __init__(self, ai):

        self.ai = ai
        self.agents = {
            "chat": ChatAgent(ai),
            "research":ResearchAgent(ai)
        }

    def choose_agent(self,task):

        message = [
            {
                "role":"system",
                "content":"""
                You are A.E.G.I.S Agent Manager.

                Choose the best agent for the user's request.

                Available agents:

                chat:
                Normal conversation, explainations, questions and general assistance.

                research: 

                Research questions and information gathering.

                Return only one word :

                Chat or Research
                """
            },
            {
                "role":"user",
                "content":task
            }
        ]

        decision = self.ai.chat(message)

        decision = decision.lower().strip()

        if "research" in decision:
            return "research"
        return "chat"

    def run(self,task):

        agent_name = self.choose_agent(task)

        agent = self.agents[agent_name]

        print(f"\n[Agent Manager: {agent.name}]")

        return agent.run(task)