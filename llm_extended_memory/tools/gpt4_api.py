"""
GPT-4 API Request
Endpoint
POST https://api.openai.com/v1/chat/completions
"""

import openai, os, json

openai.api_key = os.environ.get("OPENAI_API_KEY")

def gpt4_chat_request(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.05,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response

def decode_response(api_response):
    decoded = {
        "id": api_response["id"],
        "object": api_response["object"],
        "created": api_response["created"],
        "model": api_response["model"],
        "usage": api_response["usage"],
        "response": api_response["choices"][0]["message"]["content"],
        "finish_reason": api_response["choices"][0]["finish_reason"],
        "index": api_response["choices"][0]["index"]
    }
    return decoded

if __name__ == "__main__":
    # Sample messages for testing
    messages = [
        {"role": "system", "content": "Set the behavior"},
        {"role": "assistant", "content": "Provide examples"},
        {"role": "user", "content": "Set the instructions"}
    ]

    response = gpt4_chat_request(messages)
    decoded_response = decode_response(response)

    # Usage
    print("Decoded API response:")
    print(json.dumps(decoded_response, indent=2))