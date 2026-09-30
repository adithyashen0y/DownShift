from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

prompt = [{"role": "user", "content": "Give me a name for a coffee shop. One name only."}]

for limit in [20, 500]:
    reply = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        temperature=0,
        max_completion_tokens=limit,
    )
    choice = reply.choices[0]
    print(f"\n--- limit {limit} ---")
    print("answer:", repr(choice.message.content))
    print("finish_reason:", choice.finish_reason)
    print("usage:", reply.usage.completion_tokens, "output tokens,",
        reply.usage.completion_tokens_details.reasoning_tokens, "reasoning")