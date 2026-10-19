import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": "Explain what an API is in three simple sentences.",
        }
    ],
)

print("Response ID:", message.id)
print("Model:", message.model)
print("Role:", message.role)

print("\nClaude's response:")

for block in message.content:
    if block.type == "text":
        print(block.text)

print("\nToken usage:")
print("Input tokens:", message.usage.input_tokens)
print("Output tokens:", message.usage.output_tokens)