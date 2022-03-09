import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette(debug=True)

@app.route('/chatEvent', methods=['POST'])
async def chatEvent(request):
    data = request.json
    print(data)
    return JSONResponse({"data": "message sent"})


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)