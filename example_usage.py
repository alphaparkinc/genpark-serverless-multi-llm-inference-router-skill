from client import ServerlessMultiLlmInferenceRouterClient

def main():
    client = ServerlessMultiLlmInferenceRouterClient()
    res = client.route_inference("Summarize the quarterly financial report", 250)
    print(f"Selected Provider: {res['selected_provider']} (Latency: {res['latency_ms']}ms)")
    print(f"Response: {res['response_text']}")

if __name__ == "__main__":
    main()
