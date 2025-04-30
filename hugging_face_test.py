import os
from dotenv import load_dotenv
load_dotenv()

from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference"
)

completion = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
    max_tokens=50,
)

print(completion.choices[0].message)
print(type(completion.choices[0].message))