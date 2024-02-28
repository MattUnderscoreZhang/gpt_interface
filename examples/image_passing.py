from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


def ask_about_image_from_filepath():
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4-vision-preview",
    )
    interface.append_image_to_log_from_filepath("tests/elephant.webp")
    response = interface.say("What animal is this?")
    print(response)


def ask_about_image_from_url():
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4-vision-preview",
    )
    interface.append_image_to_log_from_url("https://en.wikipedia.org/static/images/icons/wikipedia.png")
    response = interface.say("What logo is this?")
    print(response)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    ask_about_image_from_filepath()
    ask_about_image_from_url()
