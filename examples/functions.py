from dotenv import load_dotenv
import os
from print_columns import print_columns
from typing import cast, Literal

from gpt_interface import GptInterface
from gpt_interface.tools import make_annotated_function


def get_function_call_with_optional_params() -> None:
    def convert_day_to_int(day: Literal["M", "T", "W", "Th", "F", "Sa", "Su"], one_index: bool = False) -> int:
        return ["M", "T", "W", "Th", "F", "Sa", "Su"].index(day) + one_index

    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_tools(
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
    def print_and_confirm(strings: list[str], column_widths: list[int], colors: list[str], divider: str = " | ") -> str:
        print_columns(strings, column_widths, colors, divider)
        return "Printing complete"

    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-4",
    )
    interface.set_tools(
        [
            make_annotated_function(
                print_and_confirm,
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
    get_function_call_with_optional_params()
    call_external_function()
