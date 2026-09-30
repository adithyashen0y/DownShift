from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

MODELS = {
    "cheap": "gemini-3.5-flash-lite",
    "strong": "openai/gpt-oss-120b",
}

prompt = "Say hello in five words."

gemini = genai.Client()
cheap = gemini.models.generate_content(model=MODELS["cheap"], contents=prompt)
print("cheap  ->", cheap.text)

groq = Groq()
strong = groq.chat.completions.create(
    model=MODELS["strong"],
    messages=[{"role": "user", "content": prompt}],
)
print("strong ->", strong.choices[0].message.content)

print("\n--- token usage ---")
print("cheap :", cheap.usage_metadata)
print("strong:", strong.usage)