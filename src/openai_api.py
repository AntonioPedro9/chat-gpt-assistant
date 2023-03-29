import openai
from dotenv import load_dotenv
import os

load_dotenv()

def query_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,
    )

    message = response.choices[0].text

    return message
