from openai import OpenAI

class Solar:
    """Implementation of the Solar LLM Class.
    
    Attributes:
        api_key: The API Key.
        client: Client for communicating with Solar.
        model: The solar model (set at solar-1-mini-chat)
    """

    def __init__(self, api_key: str) -> None:
        """Take in an API Key and initialize the Solar LLM Class.
        
        Attributes:
            api_key: The API Key of the Solar LLM Class.
        """

        self.client = OpenAI(api_key = api_key, base_url = "https://api.upstage.ai/v1/solar")
        self.model = "solar-1-mini-chat"

    def message(self, message: str) -> str:
        """Take in a message and chat with Solar LLM to return a message.

        Attributes:
            message: The message that is being sent to Solar LLM.
        """

        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant." # Please Put Default Prompt Here
            },
            {
                "role": "user",
                "content": "\n".join(message)
            }
        ] 

        stream = self.client.chat.completions.create(
            model = self.model,
            messages = messages,
            stream = True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")