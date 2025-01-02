import json
from groq_client import GroqClient
from extractor import extract_information, convert_to_json

def main():
    # Sample Queries
    queries = [
        "Get me Flipkart's GMV for the last quarter",
        "What was Amazon's revenue in 2021?"
    ]

    client = GroqClient(api_key="your_api_key_here")

    for query in queries:
        extracted_info = extract_information(query)
        json_data = convert_to_json(extracted_info)
        response = client.call_llm_api(query)

        print(f"Query: {query}")
        print("Extracted Info:", json.dumps(extracted_info, indent=2))
        print("JSON Data:", json.dumps(json_data, indent=2))
        print("API Response:", response)
        print("\n")

if __name__ == "__main__":
    main()
