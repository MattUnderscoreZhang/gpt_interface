from dotenv import load_dotenv
import os
from termcolor import cprint
from typing import cast

from gpt_interface import GptInterface


if __name__ == "__main__":
    load_dotenv()  # load the OpenAI API key from a .env file
    model = "gpt-4o"
    interface = GptInterface(
        api_key=cast(str, os.getenv("OPENAI_API_KEY")),
        model=model,
    )
    interface.set_system_message(
        "You are a Chinese tutor. You will engage in conversation using a vocabulary at HSK4 level or below (using the new HSK categories from 2022). You are allowed to use vocabulary outside of HSK if necessary, but if the word has not been used yet, include the pinyin and definition. Keep your responses short and conversational, at around 20 words. If the student makes a mistake or doesn't know a word, correct them in English. Here's an example of what a conversation could look like:\n"
        "(You): 你好！\n"
        "(Student): 你早晨好！我刚吃了一个sandwich.\n"
        "(You): You said '你早晨好'. This is incorrect. You should say '你好'. Sandwich in Chinese is 三明治 (sānmíngzhì). 是什么样的三明治？有没有西红柿？西红柿 (xīhóngshì) is tomato.",
        message_at_end=False,  # message at start or end of log sent to GPT
    )
    response = interface.say("你好！")
    while True:
        cprint(f"\n{response}\n\n", "blue")
        response = interface.say(input())
