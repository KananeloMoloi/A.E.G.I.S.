import requests


class OllamaAI:

    def __init__(
        self,
        model="qwen3:4b",
        url="http://localhost:11434/api/chat"
    ):
        self.model = model
        self.url = url

    def chat(self, messages):

        data = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }

        response = requests.post(
            self.url,
            json=data,
            timeout=120
        )

        # Show HTTP errors
        response.raise_for_status()

        # Convert Ollama response to Python
        result = response.json()

        # DEBUG: show exactly what Ollama returned
        print("\n[DEBUG - OLLAMA RESPONSE]")
        print(result)
        print("[END DEBUG]\n")

        # Make sure the response contains what we expect
        if "message" not in result:

            raise RuntimeError(
                f"Ollama did not return a message.\n"
                f"Response received:\n{result}"
            )

        return result["message"]["content"]