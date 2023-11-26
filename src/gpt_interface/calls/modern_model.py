import json
from openai import OpenAI
from typing import cast, Any

from gpt_interface.log import Log
from gpt_interface.options.functions import AnnotatedFunction
from gpt_interface.options.system_message import SystemMessageOptions


def call_modern_model(
    interface: OpenAI,
    model: str,
    log: Log,
    temperature: float,
    system_message_options: SystemMessageOptions,
    json_mode: bool,
    annotated_functions: list[AnnotatedFunction],
) -> str:
    #================================
    # assemble log and system message
    #================================
    messages=[
        {
            "role": message.role,
            "content": message.content
        }
        for message in log.messages
    ]
    if system_message_options.use_system_message:
        system_message = {
            "role": "system",
            "content": system_message_options.system_message,
        }
        if system_message_options.message_at_end:
            messages.append(system_message)
        else:
            messages.insert(0, system_message)
    #======================================
    # set arguments for completion endpoint
    #======================================
    completion_args = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }
    if json_mode and model in ["gpt-3.5-turbo-1106", "gpt-4-1106-preview"]:
        completion_args["response_format"] = { "type": "json_object" }
    if len(annotated_functions) > 0:
        completion_args["functions"] = [
            function.annotation
            for function in annotated_functions
        ]
    #=======================
    # get and parse response
    #=======================
    response = interface.chat.completions.create(**completion_args)
    if response.choices[0].finish_reason == "function_call":
        # https://platform.openai.com/docs/guides/function-calling
        function_call = cast(Any, response.choices[0].message.function_call)
        return_message = f"{function_call.name}({function_call.arguments})"
    else:
        return_message = response.choices[0].message.content
    return return_message if return_message else "[ERROR: NO RESPONSE]"


"""
def auto_call_function() -> None:
    function_call = cast(Any, response.choices[0].message.function_call)
    log.append("assistant", f"{function_call.name}({function_call.arguments})")
    matching_function = [
        function.function
        for function in annotated_functions
        if function.annotation["name"] == function_call.name
    ][0]
    function_return = matching_function(**json.loads(function_call.arguments))
    log.append("assistant", f"I should tell the user that the function returned the following:\n{function_return}")
    return_message = call_modern_model(
        interface=interface,
        model=model,
        log=log,
        system_message_options=system_message_options,
        temperature=temperature,
        json_mode=json_mode,
        annotated_functions=annotated_functions,
    )
    log.append("assistant", return_message)
"""
