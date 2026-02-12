# API Documentation

## Endpoints

### POST /api/chat

Stream chat completions using the Data Stream Protocol.

**Request Body:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you?"
    }
  ]
}
```

**Query Parameters:**

- `protocol` (optional): Stream protocol to use. Default: `"data"`
  - `"data"`: Data Stream Protocol (recommended)
  - `"text"`: Plain text streaming

**Response:**

- Content-Type: `text/event-stream`
- Server-Sent Events (SSE) stream

**Example:**

```bash
curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "What is the weather in San Francisco?"
      }
    ]
  }'
```

## Message Format

### ClientMessage

```typescript
interface ClientMessage {
  role: "user" | "assistant" | "system";
  content?: string;
  parts?: ClientMessagePart[];
  experimental_attachments?: ClientAttachment[];
  toolInvocations?: ToolInvocation[];
}
```

### ClientMessagePart

```typescript
interface ClientMessagePart {
  type: string;
  text?: string;
  contentType?: string;
  url?: string;
  data?: any;
  toolCallId?: string;
  toolName?: string;
  state?: string;
  input?: any;
  output?: any;
  args?: any;
}
```

## Available Tools

### get_current_weather

Get the current weather at a location.

**Parameters:**

- `latitude` (number): The latitude of the location
- `longitude` (number): The longitude of the location

**Returns:**

```json
{
  "current": {
    "temperature_2m": 18.5
  },
  "daily": {
    "sunrise": ["2024-01-01T07:00:00"],
    "sunset": ["2024-01-01T17:00:00"]
  }
}
```

**Example:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "What's the weather in New York?"
    }
  ]
}
```

## Error Handling

The API returns errors in the following format:

```json
{
  "error": {
    "message": "Error description",
    "type": "error_type",
    "code": "error_code"
  }
}
```

Common error codes:

- `400`: Bad Request - Invalid message format
- `429`: Too Many Requests - Rate limit exceeded
- `500`: Internal Server Error - Server error

## Rate Limiting

Currently, rate limiting is handled by the OpenAI API through Vercel AI Gateway.

## Authentication

In production, authentication is handled via Vercel OIDC. For local development, you can use a direct OpenAI API key in your `.env.local` file.
