from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

response = client.responses.create(
    model="llama3.1:latest",
    instructions="You are a funny assistant.",
    input="tell me capital of France ?",
)

print(response.output_text)