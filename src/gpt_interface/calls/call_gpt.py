from openai import OpenAI

from gpt_interface.calls.legacy_model import call_legacy_model
from gpt_interface.calls.modern_model import call_modern_model
from gpt_interface.log import Log
from gpt_interface.options.functions import AnnotatedFunction
from gpt_interface.options.models import known_models
from gpt_interface.options.system_message import SystemMessageOptions


def call_gpt(
    interface: OpenAI,
    model: str,
    log: Log,
    temperature: float,
    system_message_options: SystemMessageOptions,
    json_mode: bool,
    annotated_functions: list[AnnotatedFunction],
) -> str:
    if model in [m.name for m in known_models if not m.legacy_chat_api]:
        return call_modern_model(
            interface=interface,
            model=model,
            log=log,
            temperature=temperature,
            system_message_options=system_message_options,
            json_mode=json_mode,
            annotated_functions=annotated_functions,
        )
    elif model in [m.name for m in known_models]:
        return call_legacy_model(
            interface=interface,
            model=model,
            log=log,
            temperature=temperature,
            system_message_options=system_message_options,
        )
    else:
        raise ValueError(f"Unrecognized model: {model}")
