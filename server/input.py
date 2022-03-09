# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = dialo_gpt_input_from_dict(json.loads(json_string))

from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Inputs:
    generated_responses: List[Any]
    past_user_inputs: List[Any]
    text: str

    def __init__(self, generated_responses: List[Any], past_user_inputs: List[Any], text: str) -> None:
        self.generated_responses = generated_responses
        self.past_user_inputs = past_user_inputs
        self.text = text

    @staticmethod
    def from_dict(obj: Any) -> 'Inputs':
        assert isinstance(obj, dict)
        generated_responses = from_list(lambda x: x, obj.get("generated_responses"))
        past_user_inputs = from_list(lambda x: x, obj.get("past_user_inputs"))
        text = from_str(obj.get("text"))
        return Inputs(generated_responses, past_user_inputs, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generated_responses"] = from_list(lambda x: x, self.generated_responses)
        result["past_user_inputs"] = from_list(lambda x: x, self.past_user_inputs)
        result["text"] = from_str(self.text)
        return result


class DialoGPTInput:
    inputs: Inputs

    def __init__(self, inputs: Inputs) -> None:
        self.inputs = inputs

    @staticmethod
    def from_dict(obj: Any) -> 'DialoGPTInput':
        assert isinstance(obj, dict)
        inputs = Inputs.from_dict(obj.get("inputs"))
        return DialoGPTInput(inputs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["inputs"] = to_class(Inputs, self.inputs)
        return result


def dialo_gpt_input_from_dict(s: Any) -> DialoGPTInput:
    return DialoGPTInput.from_dict(s)


def dialo_gpt_input_to_dict(x: DialoGPTInput) -> Any:
    return to_class(DialoGPTInput, x)
