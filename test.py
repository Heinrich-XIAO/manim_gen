from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="thanhkt/codegemma-7B-ManimGen")
pipe(messages)
