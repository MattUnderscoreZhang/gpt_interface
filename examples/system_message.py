from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


def be_pirate():
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_system_message("You will respond as a 19th century pirate. You only speak in the form of lyrics from sea shanties.")
    interface.say("What's your job?")
    interface.say("What year is it?")
    print(interface.log)


def be_space_trucker():
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_system_message("You will respond as a 23rd century space trucker. You talk like a hard-boiled detective. Keep your responses short.")
    interface.say("What's your job?")
    interface.say("What year is it?")
    print(interface.log)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    be_pirate()
    print()
    be_space_trucker()
