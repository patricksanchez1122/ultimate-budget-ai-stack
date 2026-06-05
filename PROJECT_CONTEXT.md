# AI Stack Project Context

## Architecture
- **Proxy**: LiteLLM running at `http://localhost:4000`.
- **Target**: Gemini API (via `gemini/gemini-3.5-flash`).
- **Configuration**: `config\litellm-router.yaml` handles model mapping.

## Canonical Commands
- **Start Proxy**: `litellm --config config\litellm-router.yaml --port 4000`
- **Test Command**:
  Invoke-RestMethod -Uri "http://localhost:4000/v1/chat/completions" -Method Post -ContentType "application/json" -Body '{ "model": "gemini-3.5-flash", "messages": [{"role": "user", "content": "Hi"}] }'

## Strands SDK Configuration
- Must set: `litellm.use_litellm_proxy = True`
- Must set: `client_args = {"base_url": "http://localhost:4000"}`
- Model ID: `gemini-3.5-flash`