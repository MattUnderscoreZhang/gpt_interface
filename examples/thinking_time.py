from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface


def dont_think(question: str):
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
        json_mode=True,
    )
    interface.say(question)
    print(interface.log)


def think(question: str):
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
        json_mode=True,
    )
    interface.say(question, thinking_time=300)
    print(interface.log)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    question = """
A farmer is looking to divide his land among his three children. The land is a rectangle, 600 meters long and 400 meters wide. The eldest child wants a piece of land that is exactly twice the size of the land given to the youngest. The middle child is happy with any size of land. How should the farmer divide his land so that each child gets a fair share, with the eldest getting twice as much as the youngest, and the middle child getting an equal share?
    """
    dont_think(question)
    think(question)
