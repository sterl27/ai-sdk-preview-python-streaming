from api.utils.prompt import (
    ClientMessage,
    ClientMessagePart,
    ToolInvocation,
    ToolInvocationState,
    convert_to_openai_messages,
)


def test_simple_text_message():
    """Test conversion of a simple text message"""
    messages = [ClientMessage(role="user", content="Hello, world!")]

    result = convert_to_openai_messages(messages)

    assert len(result) == 1
    assert result[0]["role"] == "user"
    assert result[0]["content"] == "Hello, world!"


def test_message_with_parts():
    """Test conversion of message with text parts"""
    messages = [
        ClientMessage(
            role="user", parts=[ClientMessagePart(type="text", text="What is the weather?")]
        )
    ]

    result = convert_to_openai_messages(messages)

    assert len(result) == 1
    assert result[0]["role"] == "user"
    assert result[0]["content"] == "What is the weather?"


def test_message_with_tool_invocation():
    """Test conversion of message with tool invocation"""
    messages = [
        ClientMessage(
            role="assistant",
            toolInvocations=[
                ToolInvocation(
                    state=ToolInvocationState.CALL,
                    toolCallId="call_123",
                    toolName="get_current_weather",
                    args={"latitude": 37.7749, "longitude": -122.4194},
                    result=None,
                )
            ],
        )
    ]

    result = convert_to_openai_messages(messages)

    # Should have assistant message with tool call + tool result message
    assert len(result) == 2
    assert result[0]["role"] == "assistant"
    assert "tool_calls" in result[0]
    assert result[0]["tool_calls"][0]["function"]["name"] == "get_current_weather"


def test_empty_message():
    """Test conversion of empty message"""
    messages = [ClientMessage(role="user")]

    result = convert_to_openai_messages(messages)

    assert len(result) == 1
    assert result[0]["role"] == "user"
    assert result[0]["content"] == ""


def test_multiple_messages():
    """Test conversion of multiple messages"""
    messages = [
        ClientMessage(role="user", content="Hello"),
        ClientMessage(role="assistant", content="Hi there!"),
        ClientMessage(role="user", content="How are you?"),
    ]

    result = convert_to_openai_messages(messages)

    assert len(result) == 3
    assert result[0]["role"] == "user"
    assert result[1]["role"] == "assistant"
    assert result[2]["role"] == "user"
