from dotenv import load_dotenv
import os
from termcolor import cprint
from typing import cast

from gpt_interface import GptInterface


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    model = "gpt-4o"
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model=model,
    )
    cprint(f"You are talking to {model}.\n", "blue")
    while True:
        response = interface.say(input())
        cprint(f"\n{response}\n\n", "blue")
