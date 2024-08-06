from predibase import Predibase, FinetuningConfig, DeploymentConfig
import pandas as pd
import datetime

class Predibase:
    """Implementation of the predibase class.
    
    Attributes:
        api_token: API Token from Predibase.
        adapter_id: The ID for the adapter
        max_new_tokens: The maximum number of tokens.
        client: The Predibase client.
    """

    def __init__(self, api_token: str, adapter_id: str, max_new_tokens: int = 1000) -> None:
        """Take in an API token and initialize Predibase class.
        
        Attributes:
            api_token: API Token from Predibase.
            adapter_id: The adapter ID.
            max_new_tokens: The maximum number of tokens.
        """

        self.client = Predibase(api_token = api_token)
        self.adapter_id = adapter_id
        self.max_new_tokens = max_new_tokens

    def _sentiment(self, review: str) -> int:
        """Take in a single review and return a sentiment rating.
        
        Attributes:
            review: The review.
        """

        input_prompt = f"""
            <|im_start|>system\nThe following is a review from locals or people from authority to tour companies. Please give it an overall sentiment rating, from 0 to 10 of the review, where 0 denotes a completely negative experience, while 10 denotes a completely positive experience.<|im_end|>
            <|im_start|>passage
            {review}<|im_end|>
            <|im_start|>rating
            """
        
        return input_prompt
    
    def sentiment(self, data: dict) -> pd.DataFrame:
        """Take in a data of texts and return a dataframe of sentiments.

        Attributes:
            data: Dictionary of a single row of data inside a database.
        
        Pre-Condition: Must include a category, time (timestamp), feedback and sentiment, and 1 row.
        """

        feedback = self._sentiment(data['feedback'])
        lorax_client = self.client.deployments.client("solar-1-mini-chat-240612")
        sentiment = lorax_client.generate(feedback, adapter_id=self.adapter_id, max_new_tokens=self.max_new_tokens).generated_text

        processed_data = {
            'feedback': [data['feedback']],
            'time': [data['time']],
            'category': [data['category']],
            'sentiment': [sentiment]
        }

        return pd.DataFrame(processed_data)







