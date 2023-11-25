from dotenv import load_dotenv
import os
from random import randint
from typing import cast, Literal

from gpt_interface import GptInterface
from gpt_interface.functions import describe_function


def call_simple_function() -> None:
    def get_encrypted_message(message: str) -> str:
        encrypted_message = message[::-1]
        return encrypted_message

    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_functions(
        [
            describe_function(
                get_encrypted_message,
                description="Encrypt a message",
                param_descriptions={
                    "message": "The message to encrypt",
                },
            ),
        ]
    )
    response = interface.say("Encypt the message 'Hello, world!'")
    breakpoint()


def call_complex_function() -> None:
    def convert_day_to_int(day: Literal["M", "T", "W", "Th", "F", "Sa", "Su"], random: bool = False) -> int:
        if random:
            return randint(0, 6)
        return ["M", "T", "W", "Th", "F", "Sa", "Su"].index(day)

    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_functions(
        [
            describe_function(
                convert_day_to_int,
                description="Convert a day of the week to an integer",
                param_descriptions={
                    "day": "The day of the week",
                    "random": "Whether to return a random integer",
                },
                param_types={
                    "day": "string",
                },
                param_allowed_values={
                    "day": ["M", "T", "W", "Th", "F", "Sa", "Su"],
                },
            ),
        ]
    )
    response = interface.say("Convert Monday to an integer")
    breakpoint()


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    call_simple_function()
    call_complex_function()
