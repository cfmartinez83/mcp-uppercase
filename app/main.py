from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def handle_rpc(request: Request):
    body = await request.json()

    if body.get("jsonrpc") != "2.0":
        return JSONResponse({"error": "Invalid JSON-RPC version"}, status_code=400)

    method = body.get("method")
    params = body.get("params", {})
    request_id = body.get("id")

    if method == "uppercase":
        text = params.get("text", "")
        result = text.upper()
        return {
            "jsonrpc": "2.0",
            "result": result,
            "id": request_id
        }

    return {
        "jsonrpc": "2.0",
        "error": {"code": -32601, "message": "Method not found"},
        "id": request_id
    }
