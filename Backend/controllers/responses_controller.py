import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[],
  temperature=1,
  max_tokens=203,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)