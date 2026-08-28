from agents.base import Agent


class ResearchAgent(Agent):

    def __init__(self, ai):

        super().__init__(
            name = "Reasearch Agent",
            description = "Handles research and information gathering"
        )

        self.ai = ai

    def run(self, task):

        messages = [
            {
                "role":"system",
                "content":"""
                You are A.E.G.I.S Research Agent.

                Your Job is to ananlyse resarch requests.

                You currently do not have internet access.

                Do not pretend that you searched the internet.

                Explain what information would need to be researched and provide your best knowledge whe approached
                """
            },
            {
                "role":"system",
                "content":task
            }
        ]

        return self.ai.chat(messages)