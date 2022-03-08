# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = dialo_gpt_response_from_dict(json.loads(json_string))

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


class Conversation:
    generated_responses: List[str]
    past_user_inputs: List[str]

    def __init__(self, generated_responses: List[str], past_user_inputs: List[str]) -> None:
        self.generated_responses = generated_responses
        self.past_user_inputs = past_user_inputs

    @staticmethod
    def from_dict(obj: Any) -> 'Conversation':
        assert isinstance(obj, dict)
        generated_responses = from_list(from_str, obj.get("generated_responses"))
        past_user_inputs = from_list(from_str, obj.get("past_user_inputs"))
        return Conversation(generated_responses, past_user_inputs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generated_responses"] = from_list(from_str, self.generated_responses)
        result["past_user_inputs"] = from_list(from_str, self.past_user_inputs)
        return result


class DialoGPTResponse:
    generated_text: str
    conversation: Conversation
    warnings: List[str]

    def __init__(self, generated_text: str, conversation: Conversation, warnings: List[str]) -> None:
        self.generated_text = generated_text
        self.conversation = conversation
        self.warnings = warnings

    @staticmethod
    def from_dict(obj: Any) -> 'DialoGPTResponse':
        assert isinstance(obj, dict)
        generated_text = from_str(obj.get("generated_text"))
        conversation = Conversation.from_dict(obj.get("conversation"))
        warnings = from_list(from_str, obj.get("warnings"))
        return DialoGPTResponse(generated_text, conversation, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["generated_text"] = from_str(self.generated_text)
        result["conversation"] = to_class(Conversation, self.conversation)
        result["warnings"] = from_list(from_str, self.warnings)
        return result


def dialo_gpt_response_from_dict(s: Any) -> DialoGPTResponse:
    return DialoGPTResponse.from_dict(s)


def dialo_gpt_response_to_dict(x: DialoGPTResponse) -> Any:
    return to_class(DialoGPTResponse, x)
