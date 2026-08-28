from agents.base import Agent

class ChatAgent(Agent):

    def __init__(self,ai):

        super().__init__(
            name="Chat Agent",
            description="Handles normal conversations and questions"
        )

        self.ai = ai
    def run(self,task):

        messages = [
            {
                "role":"system",
                "content":"""
                YOu are A.E.G.I.S, a friendly personal AI assistant.

                Be helpful, intelligent, calm, and professional.

                Answer the user's question naturally.

                Do not pretend that you performed an action when you did not actually perform it.
                """

            },
            {
                "role":"user",
                "content":task
            }
        ]

        return self.ai.chat(messages)