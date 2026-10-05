import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN not found in .env")

client = InferenceClient(
    api_key=token,
    provider="auto",
)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful tutor."
        },
        {
            "role": "user",
            "content": "Explain photosynthesis in one simple sentence."
        }
    ],
    max_tokens=100,
)

print(response.choices[0].message.content)