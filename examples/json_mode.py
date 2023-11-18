from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


def json_response():
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4",
        json_mode=True,
    )
    interface.set_system_message(
        "Reply in the form {'query': [user query], 'answer': [your response]}.",
    )
    interface.say("Hello.")
    interface.set_json_mode(False)
    interface.set_system_message(
        use_system_message=False,
    )
    interface.say("Say hello normally.")
    print(interface.log)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    json_response()
