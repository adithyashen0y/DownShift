from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()  # automatically uses GROQ_API_KEY

for model in client.models.list().data:
    print(model.id)