from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi import Request as FastAPIRequest
from fastapi.responses import StreamingResponse
from openai import OpenAI
from pydantic import BaseModel
from vercel import oidc
from vercel.headers import set_headers

from .utils.gemini_stream import patch_gemini_response_with_headers, stream_gemini_text
from .utils.prompt import ClientMessage, convert_to_openai_messages
from .utils.stream import patch_response_with_headers, stream_text
from .utils.tools import AVAILABLE_TOOLS, TOOL_DEFINITIONS

load_dotenv(".env.local")

app = FastAPI()


@app.middleware("http")
async def _vercel_set_headers(request: FastAPIRequest, call_next):
    set_headers(dict(request.headers))
    return await call_next(request)


class Request(BaseModel):
    messages: list[ClientMessage]


@app.post("/api/chat")
async def handle_chat_data(request: Request, protocol: str = Query("data")):
    """OpenAI chat endpoint (default)"""
    messages = request.messages
    openai_messages = convert_to_openai_messages(messages)

    client = OpenAI(
        api_key=oidc.get_vercel_oidc_token(), base_url="https://ai-gateway.vercel.sh/v1"
    )
    response = StreamingResponse(
        stream_text(client, openai_messages, TOOL_DEFINITIONS, AVAILABLE_TOOLS, protocol),
        media_type="text/event-stream",
    )
    return patch_response_with_headers(response, protocol)


@app.post("/api/chat/gemini")
async def handle_gemini_chat(request: Request, protocol: str = Query("data")):
    """
    Gemini Alic3X v2.6 chat endpoint

    Provides:
    - Decision support with real-time validation
    - RAG-driven cross-referencing
    - Structured workflow automation
    - Multi-model orchestration
    """
    messages = request.messages

    # Convert to simple message format for Gemini
    gemini_messages = []
    for msg in messages:
        if msg.content:
            gemini_messages.append({"role": msg.role, "content": msg.content})
        elif msg.parts:
            # Extract text from parts
            text_parts = [p.text for p in msg.parts if hasattr(p, "text") and p.text]
            if text_parts:
                gemini_messages.append({"role": msg.role, "content": " ".join(text_parts)})

    response = StreamingResponse(
        stream_gemini_text(
            gemini_messages,
            tool_definitions=TOOL_DEFINITIONS,
            available_tools=AVAILABLE_TOOLS,
            protocol=protocol,
            model_name="gemini-2.0-flash-exp",
        ),
        media_type="text/event-stream",
    )
    return patch_gemini_response_with_headers(response, protocol)
