from dotenv import load_dotenv
import os

from gpt_interface import GptInterface


if __name__ == "__main__":
    load_dotenv()  # Load the OpenAI API key from a .env file
    interface = GptInterface(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
