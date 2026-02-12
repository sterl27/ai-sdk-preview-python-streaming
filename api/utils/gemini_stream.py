"""
Gemini streaming utilities for Alic3X v2.6 framework
"""

import json
import traceback
import uuid
from typing import Any

from fastapi.responses import StreamingResponse

from .gemini_client import get_gemini_client


def stream_gemini_text(
    messages: list[dict[str, Any]],
    tool_definitions: list[dict[str, Any]] | None = None,
    available_tools: dict[str, Any] | None = None,
    protocol: str = "data",
    model_name: str = "gemini-2.0-flash-exp",
):
    """
    Stream text from Gemini API using Alic3X v2.6 principles

    Args:
        messages: List of message dictionaries
        tool_definitions: Optional tool definitions
        available_tools: Optional available tools mapping
        protocol: Stream protocol ("data" or "text")
        model_name: Gemini model to use

    Yields:
        Server-Sent Events formatted responses
    """

    def format_sse(payload: dict) -> str:
        """Format payload as Server-Sent Event"""
        return f"data: {json.dumps(payload)}\n\n"

    try:
        client = get_gemini_client(model_name)
        message_id = str(uuid.uuid4())

        # Start streaming
        yield format_sse({"type": "start", "messageId": message_id})

        # Stream response from Gemini
        full_text = ""
        for chunk_text in client.generate_stream(messages, tool_definitions):
            full_text += chunk_text

            # Send text delta
            yield format_sse(
                {
                    "type": "text-delta",
                    "textDelta": chunk_text,
                }
            )

        # Send finish event
        finish_metadata = {
            "finishReason": "stop",
        }

        yield format_sse(
            {
                "type": "finish",
                "messageId": message_id,
                **finish_metadata,
            }
        )

    except Exception as e:
        error_message = f"Error in Gemini streaming: {str(e)}"
        print(error_message)
        traceback.print_exc()

        yield format_sse(
            {
                "type": "error",
                "error": error_message,
            }
        )


def patch_gemini_response_with_headers(
    response: StreamingResponse,
    protocol: str = "data",
) -> StreamingResponse:
    """
    Apply standard streaming headers for Gemini responses

    Args:
        response: FastAPI StreamingResponse
        protocol: Stream protocol

    Returns:
        StreamingResponse with headers
    """
    response.headers["Content-Type"] = "text/event-stream"
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Connection"] = "keep-alive"
    response.headers["X-Vercel-AI-Data-Stream"] = "v1"

    return response
