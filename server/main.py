import requests
from input import DialoGPTInput, Inputs
from response import DialoGPTResponse, dialo_gpt_response_from_dict


def query_huggingface_dialogpt(json_data: DialoGPTInput) -> DialoGPTResponse:
    response = requests.post(
        'https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium', json=json_data.to_dict())
    json_dict = response.json()
    result = dialo_gpt_response_from_dict(json_dict)
    return result  #


json_data = DialoGPTInput(inputs=Inputs(
    generated_responses=["I\'m good, how are you?"], past_user_inputs=["Hey my name is Julien! How are you?"], text="Good good thanks"))

response = query_huggingface_dialogpt(json_data)
print(response.conversation.generated_responses)
