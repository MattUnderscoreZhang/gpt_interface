from dotenv import load_dotenv
import os
from print_columns import print_columns
from typing import cast, Literal

from gpt_interface import GptInterface
from gpt_interface.options.functions import make_annotated_function


def get_simple_function_call() -> None:
    def get_encrypted_message(message: str) -> str:
        encrypted_message = message[::-1]
        return encrypted_message

    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_annotated_functions(
        [
            make_annotated_function(
                get_encrypted_message,
                description="Encrypt a message",
                param_descriptions={
                    "message": "The message to encrypt",
                },
                param_types={
                    "message": "string",
                },
            ),
        ]
    )
    response = interface.say("Encypt the message 'Hello, world!'")
    print(response)


def get_function_call_with_optional_params() -> None:
    def convert_day_to_int(day: Literal["M", "T", "W", "Th", "F", "Sa", "Su"], one_index: bool = False) -> int:
        return ["M", "T", "W", "Th", "F", "Sa", "Su"].index(day) + one_index

    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_annotated_functions(
        [
            make_annotated_function(
                convert_day_to_int,
                description="Convert a day of the week to an integer",
                param_descriptions={
                    "day": "The day of the week",
                    "one_index": "Whether to start counting at 1 instead of 0",
                },
                param_types={
                    "day": "string",
                    "one_index": "boolean",
                },
                param_allowed_values={
                    "day": ["M", "T", "W", "Th", "F", "Sa", "Su"],
                },
            ),
        ]
    )
    response = interface.say("Convert Monday to an integer")
    print(response)
    response = interface.say("Convert Tuesday to an integer, starting from Monday=1")
    print(response)


def call_external_function() -> None:
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4",
    )
    interface.set_annotated_functions(
        [
            make_annotated_function(
                print_columns,
                description="Divide the terminal output into columns and print one wrapped string in each column. The strings, column_widths, and colors parameters should all be lists of the same length.",
                param_descriptions={
                    "strings": "The strings to print, one for each column",
                    "column_widths": "The width of each column",
                    "colors": "The text color of each column",
                    "divider": "The divider between columns",
                },
                param_types={
                    "strings": "array[string]",
                    "column_widths": "array[integer]",
                    "colors": "array[string]",
                    "divider": "string",
                },
            ),
        ]
    )
    response = interface.say("Print lorem ipsum in three columns, with widths of 30, 20, and 50. The colors should be red, blue, and green.")
    print(response)


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    # get_simple_function_call()
    # get_function_call_with_optional_params()
    call_external_function()
