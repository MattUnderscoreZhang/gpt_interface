from dotenv import load_dotenv
import os
from pathlib import Path
from typing import cast

from gpt_interface import GptInterface


def save_log():
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4",
    )
    interface.say("Hi there!")
    my_path = Path(__file__).parent  # saves in examples/ folder
    interface.log.save(my_path / "my_log.json")


def load_log():
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4",
    )
    my_path = Path(__file__).parent
    interface.log.load(my_path / "my_log.json")
    print(interface.log)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    save_log()
    load_log()
