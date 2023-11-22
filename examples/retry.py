from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    response = interface.say("Give me a random number from 1-1000.")
    print(response)
    response = interface.retry()
    print(response)
    print(interface.log)
