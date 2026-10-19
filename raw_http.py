import os
import json
import urllib.request
import urllib.error

api_key = os.environ.get("ANTHROPIC_API_KEY")

url = "https://api.anthropic.com/v1/messages"

headers = {
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
}

payload = {
    "model": "claude-sonnet-4-6",
    "max_tokens": 200,
    "messages": [
        {
            "role": "user",
            "content": "Explain what an API is in three simple sentences.",
        }
    ],
}

request = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers=headers,
    method="POST",
)

try:
    with urllib.request.urlopen(request, timeout=60) as response:
        response_body = response.read().decode("utf-8")

        print("HTTP status:", response.status)

        data = json.loads(response_body)

        print(json.dumps(data, indent=2))

except urllib.error.HTTPError as error:
    print("HTTP status:", error.code)
    print(error.read().decode("utf-8"))

except urllib.error.URLError as error:
    print("Connection error:", error.reason)