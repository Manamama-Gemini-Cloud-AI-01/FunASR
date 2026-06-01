# FunASR

FunASR is a fundamental end-to-end speech recognition toolkit.

## Documentation
- [Installation Guide](docs/installation/README.md)
- [Model Selection](docs/model_selection.md)
- [vLLM Deployment Guide](docs/vllm_guide.md)
- [Real-time Streaming Server Guide](runtime/readme.md)

## Current Status (June 2026)
- The project has been updated to support CPU-based inference via standard `AutoModel` bypass for `vLLM` components.
- Native support for OpenAI-compatible API serving is available in `examples/openai_api/`.
- Production deployment via Kubernetes is supported for OpenAI-spec APIs.
