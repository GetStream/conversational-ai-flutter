import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from event import event_from_dict
from huggingface import query_huggingface_dialogpt
from input import DialoGPTInput, Inputs
from stream_chat import StreamChat
import os
your_api_key = os.environ.get('api_key')
your_api_secret = os.environ.get('api_secret')


chat = StreamChat(api_key=your_api_key, api_secret=your_api_secret)
app = Starlette(debug=True)


@app.route('/chatEvent', methods=['POST'])
async def chatEvent(request):
    print("new event received")
    data = await request.json()
    event = event_from_dict(data)
    if event.type == "message.new" and event.message.user.id != "eugene-goostman":
        print("new user message")
        channel = chat.channel("messaging", "my-ai-friend")
        json_data = DialoGPTInput(inputs=Inputs(
            generated_responses=[], past_user_inputs=[], text=event.message.text))

        response = query_huggingface_dialogpt(json_data)
        generated_responses = response.conversation.generated_responses
        array_length = len(generated_responses)
        last_generated_response = generated_responses[array_length - 1]
        channel.send_message(
            {"text": last_generated_response}, "eugene-goostman")
    return JSONResponse({"text": "revent received"})


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
