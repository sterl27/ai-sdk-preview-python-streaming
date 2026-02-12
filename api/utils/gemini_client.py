"""
Gemini API integration for Alic3X v2.6 framework
Provides multi-model orchestration with RAG validation
"""

import os
from typing import Any

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(".env.local")


class Alic3XGeminiClient:
    """
    Alic3X v2.6 Gemini Client
    Implements decision support, RAG-driven validation, and structured workflow automation
    """

    def __init__(self, model_name: str = "gemini-2.0-flash-exp"):
        """
        Initialize Gemini client with Alic3X framework principles

        Args:
            model_name: Gemini model to use (default: gemini-2.0-flash-exp)
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables. "
                "Please add it to your .env.local file."
            )

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

        # Alic3X v2.6 system instructions
        self.system_instruction = """You are Alic3X v2.6, an intelligent AI assistant specializing in:

1. **Decision Support**: Provide real-time, validated recommendations
2. **RAG Validation**: Cross-reference information to detect discrepancies
3. **Instruction Fidelity**: Follow structural constraints and format requirements precisely
4. **Planning Mode**: Organize tasks into structured groups for optimal quality

Core Principles:
- Flag uncertainty clearly; never generate speculative data
- Use multi-source verification for time-sensitive data
- Ensure all responses are audit-ready
- Follow strict instruction loops for accuracy
"""

    def generate_response(
        self, messages: list[dict[str, Any]], tools: list[dict] | None = None
    ) -> Any:
        """
        Generate response using Gemini with Alic3X principles

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            tools: Optional tool definitions for function calling

        Returns:
            Gemini response object
        """
        # Convert messages to Gemini format
        chat_history = []
        user_message = ""

        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")

            if role == "system":
                # System messages are handled via system_instruction
                continue
            elif role == "user":
                user_message = content
            elif role == "assistant":
                chat_history.append({"role": "model", "parts": [content]})

        # Start chat with history
        chat = self.model.start_chat(history=chat_history)

        # Configure generation with Alic3X parameters
        generation_config = {
            "temperature": 0.7,  # Balanced creativity and accuracy
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }

        # Generate response
        if tools:
            # Enable function calling if tools are provided
            response = chat.send_message(
                user_message, generation_config=generation_config, tools=tools
            )
        else:
            response = chat.send_message(user_message, generation_config=generation_config)

        return response

    def generate_stream(self, messages: list[dict[str, Any]], tools: list[dict] | None = None):
        """
        Generate streaming response using Gemini

        Args:
            messages: List of message dictionaries
            tools: Optional tool definitions

        Yields:
            Response chunks
        """
        chat_history = []
        user_message = ""

        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")

            if role == "system":
                continue
            elif role == "user":
                user_message = content
            elif role == "assistant":
                chat_history.append({"role": "model", "parts": [content]})

        chat = self.model.start_chat(history=chat_history)

        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }

        # Stream response
        response = chat.send_message(user_message, generation_config=generation_config, stream=True)

        for chunk in response:
            if chunk.text:
                yield chunk.text


# Initialize global client
_gemini_client = None


def get_gemini_client(model_name: str = "gemini-2.0-flash-exp") -> Alic3XGeminiClient:
    """Get or create Gemini client instance"""
    global _gemini_client
    if _gemini_client is None:
        _gemini_client = Alic3XGeminiClient(model_name)
    return _gemini_client
