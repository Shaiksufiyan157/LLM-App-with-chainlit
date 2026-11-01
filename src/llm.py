from openrouter import OpenRouter
import os
from dotenv import load_dotenv
from src.prompt import *
load_dotenv()

messages=[
            {"content": system_instruction, "role": "system"},
        ]
def ask_chat(messages,model="openai/gpt-oss-120b",temperature=0):
    with OpenRouter(
        api_key=os.getenv("OPENROUTER_API_KEY"),
    ) as open_router:
        res = open_router.chat.send(
            model=model,
            messages=messages,
            stream=False,
            temperature=temperature
        )
        
        print(res.choices[0].message.content) 
        return res.choices[0].message.content


