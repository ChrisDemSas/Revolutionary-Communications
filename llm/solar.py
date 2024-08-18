from openai import OpenAI

class Solar:
    """Implementation of the Solar LLM Class.
    
    Attributes:
        api_key: The API Key.
        client: Client for communicating with Solar.
        model: The solar model (set at solar-1-mini-chat)
        result: The result of the first generation.
    """

    def __init__(self, api_key: str) -> None:
        """Take in an API Key and initialize the Solar LLM Class.
        
        Attributes:
            api_key: The API Key of the Solar LLM Class.
        """

        self.client = OpenAI(api_key = api_key, base_url = "https://api.upstage.ai/v1/solar")
        self.model = "solar-1-mini-chat"
        self.result = ""
        self.history = []

    def message(self, message: str) -> str:
        """Take in a message and chat with Solar LLM to return a message.

        Attributes:
            message: The message that is being sent to Solar LLM.
        """

        messages=[
            {
                "role": "system",
                "content": "You are a consultant to a tour company." # Please Put Default Prompt Here
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

        self.history.append(messages[0])
        self.history.append(messages[1])

        response = ""

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content
        
        self.result = response
        
        return response
    
    def message_chat(self, message: str) -> str:
        """Take in a message and chat with Solar LLM to return a message.

        Attributes:
            message: The message that is being sent to Solar LLM.
        """

        PROMPT = """You came up with the following solutions to address complaints from the local community and here is the previous message you sent:
        
        {self.result}

        Now, the I would like to ask more specific questions about these solutions. 
        Please answer them as thoroughly as possible, in 200 words or less. 
        I would like to ask questions on what potential costs could occur, weaknesses or strengths of the idea or even come up with new solutions altogether.

            """

        messages=[
            {
                "role": "system",
                "content": "You are consultant to a tour company." # Please Put Default Prompt Here
            },
            {
                "role": "user",
                "content": "\n".join(message)
            }
        ] 
        self.history.append(messages[0])
        self.history.append(messages[1])

        stream = self.client.chat.completions.create(
            model = self.model,
            messages = self.history,
            stream = True
        )

        response = ""

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                response += chunk.choices[0].delta.content

        return response