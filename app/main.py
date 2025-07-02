from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from datetime import datetime

app = FastAPI()

# Enable CORS for web compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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

    # Method: get_status
    if method == "get_status":
        now = datetime.utcnow().isoformat()
        return {
            "jsonrpc": "2.0",
            "result": {
                "datetime": now,
                "code": "mcp_cristian_martinez"
            },
            "id": request_id
        }

    # Method: uppercase
    elif method == "uppercase":
        text = params.get("text")
        if not text:
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32602,
                    "message": "Missing 'text' parameter"
                },
                "id": request_id
            }
        return {
            "jsonrpc": "2.0",
            "result": text.upper(),
            "id": request_id
        }

    # Unknown method
    return {
        "jsonrpc": "2.0",
        "error": {
            "code": -32601,
            "message": f"Method '{method}' not found"
        },
        "id": request_id
    }
