import inspect
from typing import Callable


def get_param_types(func: Callable) -> dict[str, str]:
    type_mapping = {
        int: "int",
        str: "string",
        float: "float",
        # add more mappings as needed
    }
    return {
        name : (
            type_mapping.get(param.annotation, str(param.annotation))
            if param.annotation is not inspect.Parameter.empty
            else ""
        )
        for name, param in inspect.signature(func).parameters.items()
    }


def get_required_parameters(func: Callable) -> list[str]:
    return [
        name
        for name, param in inspect.signature(func).parameters.items()
        if param.default == inspect.Parameter.empty and param.kind == param.POSITIONAL_OR_KEYWORD
    ]


def get_function_dict(
    func: Callable,
    description: str,
    param_descriptions: dict[str, str],
    param_types: dict[str, str] | None = None,
    param_allowed_values: dict[str, list[str]] | None = None,
) -> dict:
    if param_types is None:
        param_types = get_param_types(func)
    func_dict = {
        "name": func.__name__,
        "description": description,
        "parameters": {
            "type": "object",
            "properties": {
                parameter: {
                    "type": param_types[parameter],
                    "description": param_descriptions.get(parameter, ""),
                }
                for parameter in func.__code__.co_varnames[
                    : func.__code__.co_argcount
                ]
            },
            "required": get_required_parameters(func),
        },
    }
    if param_allowed_values is not None:
        for parameter, allowed_values in param_allowed_values.items():
            func_dict["parameters"]["properties"][parameter]["enum"] = allowed_values
    return func_dict


# function_call={"name": "get_answer_for_user_query"}


# def get_function_call_from_message(message: dict, function: Function) -> Callable:
    # ...

# response = {
    # "role": "assistant",
    # "content": None,
    # "function_call": {
        # "name": "get_current_weather",
        # "arguments": "{ \"location\": \"Boston, MA\"}",
    # },
# }

# {"role": "function", "name": "get_current_weather", "content": "{\"temperature\": "22", \"unit\": \"celsius\", \"description\": \"Sunny\"}"}
