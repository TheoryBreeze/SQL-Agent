from dotenv import load_dotenv
load_dotenv()

import os

from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])


def llm_invoke(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=message
    )
    return response.text

