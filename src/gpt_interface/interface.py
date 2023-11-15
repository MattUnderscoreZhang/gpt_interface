import openai
from openai import OpenAI

from gpt_interface.log import Log


class GptInterface:
    def __init__(
        self,
        openai_api_key: str,
        model: str,
        json_mode: bool = False,
        temperature: float = 1.0,
        warnings: bool = True,
    ) -> None:
        openai.api_key = openai_api_key
        self.set_model(model, warnings=warnings)
        self.set_json_mode(json_mode)
        self.temperature = temperature
        self.interface = OpenAI()

    def set_model(self, model: str, warnings: bool = True) -> None:
        self.model = model
        recommended_models = [
            "gpt-3.5-turbo",
            "gpt-4",
            "gpt-4-32k",
        ]
        if warnings and (model not in recommended_models):
            print(f"WARNING: {self.model} is not recognized as a recommended model.")
            print(f"Recommended models: {recommended_models}")
            print(f"See https://platform.openai.com/docs/models for more information.")
            print(f"To deactivate this warning, set warnings=False during GptInterface initialization.")

    def set_json_mode(self, json_mode: bool) -> None:
        self.json_mode = json_mode

    def call(self, log: Log) -> str:
        if self.model.startswith("gpt-4") or self.model.startswith("gpt-3.5"):
            # modern models
            response = self.interface.chat_completions.create(
                model=self.model,
                messages=[
                    {
                        "role": message.role,
                        "content": message.content
                    }
                    for message in log
                ],
                temperature=self.temperature,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content
        elif any([
            self.model.startswith(prefix)
            for prefix in ["davinci", "curie", "babbage", "ada", "text-"]
        ]):
            # legacy models
            response = self.interface.completions.create(
                model=self.model,
                prompt="\n".join([
                    f"{message.role}: {message.content}"
                    for message in log
                ]) + "assistant: ",
                temperature=self.temperature,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            return response.choices[0].text
        else:
            return str("Unrecognized model.")
