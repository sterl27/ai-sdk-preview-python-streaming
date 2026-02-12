# Gemini Alic3X v2.6 Integration

This document describes the Gemini AI integration with the Alic3X v2.6 framework for advanced AI capabilities.

## Overview

The Gemini integration provides:
- **Decision Support**: Real-time validated recommendations
- **RAG Validation**: Cross-reference information to detect discrepancies  
- **Instruction Fidelity**: Precise format and constraint adherence
- **Planning Mode**: Structured task organization for optimal quality

## Setup

### 1. Get Gemini API Key

Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to get your API key.

### 2. Configure Environment

Add to your `.env.local` file:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## API Endpoints

### Gemini Chat Endpoint

**POST** `/api/chat/gemini`

Uses Google's Gemini 2.0 Flash model with Alic3X v2.6 framework principles.

**Request:**
```json
{
  "messages": [
    {
      "role": "user",
      "content": "What is the weather in San Francisco?"
    }
  ]
}
```

**Response:**
Server-Sent Events (SSE) stream with:
- `start`: Stream initialization
- `text-delta`: Incremental text chunks
- `finish`: Stream completion with metadata

### OpenAI Chat Endpoint (Default)

**POST** `/api/chat`

Uses OpenAI models via Vercel AI Gateway.

## Usage Examples

### Frontend Integration

```typescript
import { useChat } from '@ai-sdk/react';

function GeminiChat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    api: '/api/chat/gemini', // Use Gemini endpoint
  });

  return (
    <div>
      {messages.map(m => (
        <div key={m.id}>
          {m.role}: {m.content}
        </div>
      ))}
      
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

### Direct API Call

```bash
curl -X POST http://localhost:3000/api/chat/gemini \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Explain quantum computing"
      }
    ]
  }'
```

## Alic3X v2.6 Framework Principles

### 1. Query Intake
- Validates intent and context continuity
- Ensures message format compliance

### 2. RAG Validation
- Real-time cross-referencing
- Discrepancy detection and flagging

### 3. Instruction Fidelity
- Structural constraint enforcement
- Word limits and format validation
- Exact specification adherence

### 4. Planning Mode
- Organizes tasks into structured groups
- Ensures optimal quality through systematic processing

## Architecture

```
api/
├── index.py                    # Main FastAPI app with endpoints
└── utils/
    ├── gemini_client.py        # Alic3X Gemini client
    ├── gemini_stream.py        # Gemini streaming utilities
    ├── prompt.py               # Message conversion
    ├── stream.py               # OpenAI streaming (original)
    └── tools.py                # Tool definitions
```

## Features

### Multi-Model Support
- **Gemini 2.0 Flash**: Fast, efficient responses
- **OpenAI GPT**: Via Vercel AI Gateway
- Easy model switching via endpoint selection

### Streaming Responses
- Real-time text generation
- Server-Sent Events (SSE) protocol
- Compatible with Vercel AI SDK

### Tool Calling
- Weather API integration
- Extensible tool framework
- Automatic tool execution

## Security & Compliance

Following Alic3X v2.6 principles:

- ✅ **Uncertainty Flagging**: Never generates speculative data
- ✅ **Multi-Source Verification**: Cross-references time-sensitive information
- ✅ **Audit-Ready**: All responses traceable and verifiable
- ✅ **Strict Instruction Loops**: Ensures accuracy and compliance

## Troubleshooting

### API Key Issues

```python
ValueError: GEMINI_API_KEY not found in environment variables
```

**Solution**: Add `GEMINI_API_KEY` to your `.env.local` file.

### Import Errors

```python
ModuleNotFoundError: No module named 'google.generativeai'
```

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Streaming Issues

If streaming doesn't work, check:
1. Content-Type header is `text/event-stream`
2. Cache-Control is set to `no-cache`
3. Connection is `keep-alive`

## Performance

### Gemini 2.0 Flash
- **Latency**: ~500ms first token
- **Throughput**: ~40 tokens/second
- **Context**: 1M tokens
- **Cost**: Highly cost-effective

### Comparison with OpenAI
- **Speed**: Gemini is generally faster
- **Quality**: Comparable for most tasks
- **Cost**: Gemini is more cost-effective
- **Context**: Gemini supports larger contexts

## Best Practices

1. **Use Gemini for**:
   - High-volume applications
   - Cost-sensitive deployments
   - Large context requirements
   - Fast response needs

2. **Use OpenAI for**:
   - Specific GPT-4 capabilities
   - Existing OpenAI integrations
   - When using Vercel AI Gateway features

3. **Error Handling**:
   - Always catch and log errors
   - Provide fallback responses
   - Monitor API quotas

## Future Enhancements

- [ ] Function calling with Gemini
- [ ] Multi-modal support (images, audio)
- [ ] Caching for improved performance
- [ ] Custom safety settings
- [ ] Model fine-tuning support

## Resources

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Alic3X Framework](https://github.com/your-repo/alic3x)
- [Vercel AI SDK](https://sdk.vercel.ai/)

## License

Same as parent project.
