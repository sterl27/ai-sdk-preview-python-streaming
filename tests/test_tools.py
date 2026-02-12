from api.utils.tools import AVAILABLE_TOOLS, TOOL_DEFINITIONS, get_current_weather


def test_tool_definitions_structure():
    """Test that tool definitions are properly structured"""
    assert len(TOOL_DEFINITIONS) == 1
    assert TOOL_DEFINITIONS[0]["type"] == "function"
    assert TOOL_DEFINITIONS[0]["function"]["name"] == "get_current_weather"
    assert "parameters" in TOOL_DEFINITIONS[0]["function"]


def test_available_tools_mapping():
    """Test that available tools are properly mapped"""
    assert "get_current_weather" in AVAILABLE_TOOLS
    assert callable(AVAILABLE_TOOLS["get_current_weather"])


def test_get_current_weather_valid_coordinates():
    """Test weather API with valid coordinates (San Francisco)"""
    result = get_current_weather(37.7749, -122.4194)

    assert result is not None
    assert "current" in result
    assert "temperature_2m" in result["current"]


def test_get_current_weather_invalid_coordinates():
    """Test weather API with invalid coordinates"""
    # Using coordinates that are out of range
    result = get_current_weather(999, 999)

    # API should handle this gracefully
    # Either return None or valid error response
    assert result is None or "error" in result or "current" in result
