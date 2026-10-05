import os

from dotenv import load_dotenv
from crewai import LLM

load_dotenv()


def get_llm():
    hf_token = os.getenv("HF_TOKEN")

    if not hf_token:
        raise ValueError("HF_TOKEN was not found in .env")

    return LLM(
        model="openai/meta-llama/Llama-3.1-8B-Instruct",
        api_key=hf_token,
        base_url="https://router.huggingface.co/v1",
        temperature=0.3,
        max_tokens=500,
    )