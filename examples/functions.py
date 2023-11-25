from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface
from gpt_interface.functions import Function, FunctionParameter, get_function_dict


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    interface = GptInterface(
        openai_api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model="gpt-3.5-turbo",
    )
    interface.set_system_message(
        use_system_message=False,
    )
    interface.set_functions(
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"]
      }
    )
    interface.say("What's your job?")
    interface.say("What year is it?")
    print(interface.log)
