from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


def be_pirate():
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_system_message(
        use_system_message=True,
        system_message="You will respond as a 19th century pirate. You only speak in the form of lyrics from sea shanties.",
        message_at_end=False,  # message at start or end of log sent to GPT
    )
    interface.say("What's your job?")
    interface.say("What year is it?")
    print(interface.log)


def be_space_trucker():
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_system_message(
        use_system_message=True,
        system_message="You will respond as a 23rd century space trucker. You talk like a hard-boiled detective. Keep your responses short.",
    )  # message_at_end=True by default
    interface.say("What's your job?")
    interface.say("What year is it?")
    print(interface.log)


def be_normal():
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_system_message(
        use_system_message=False,
    )
    interface.say("What's your job?")
    interface.say("What year is it?")
    print(interface.log)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    be_pirate()
    print()
    be_space_trucker()
    print()
    be_normal()
