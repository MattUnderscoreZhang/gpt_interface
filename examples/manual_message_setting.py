from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface
from gpt_interface.log import Message


def change_name():
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4",
    )
    interface.say("Hi there!")
    interface.say("My first name is Bob.")
    interface.say("My last name is Smith.")
    messages = interface.log.messages[:-2]  # remove last user message and GPT reply
    interface.log.set_messages(messages)
    interface.say("My last name is Jones.")
    print(interface.log)


def force_response():
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4",
    )
    messages = [
        Message(
            role="user",
            content="What's the square root of 4?",
        ),
        Message(
            role="assistant",
            content="I believe the square root of 4 is 3.",
        ),
    ]
    interface.log.set_messages(messages)
    interface.say("Is that correct?")
    print(interface.log)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    change_name()
    print()
    force_response()
