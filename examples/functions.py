from dotenv import load_dotenv
import os
from typing import cast

from gpt_interface import GptInterface
from gpt_interface.functions import get_function_dict


def get_encrypted_message(message: str) -> str:
    encrypted_message = message[::-1]
    return encrypted_message


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
        [
            get_function_dict(
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
