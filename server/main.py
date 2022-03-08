import requests

json_data = {
    'inputs': {
        'generated_responses': [
            'I\'m good, how are you?',
        ],
        'past_user_inputs': [
            'Hey my name is Julien! How are you?',
        ],
        'text': 'Good good thanks',
    },
}

response = requests.post(
    'https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium', json=json_data)
print(response.text)
# {"generated_text":"No problem, I'm glad you're doing well!","conversation":{"generated_responses":["I'm good, how are you?","No problem, I'm glad you're doing well!"],"past_user_inputs":["Hey my name is Julien! How are you?","Good good thanks"]},"warnings":["Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation."]}
