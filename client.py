class ServerlessMultiLlmInferenceRouterClient:
    def route_inference(self, prompt: str, preferred_latency_ms: int = 200) -> dict:
        provider = "DigitalOcean-Inference-Node-East" if preferred_latency_ms < 300 else "Cloud-Fallback-Endpoint"
        return {
            "selected_provider": provider,
            "response_text": f"Inference completion for '{prompt[:30]}...' via {provider}.",
            "latency_ms": 145
        }
