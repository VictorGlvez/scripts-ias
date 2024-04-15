from openai import OpenAI


client = OpenAI(
    base_url="http://127.0.0.1:8081/v1",
    api_key = "sk-no-key-required")

messages = [
    {"role": "system", "content": "Eres un Asistente"},
    {"role": "user", "content": "Quiero que solo me devuelvas el clima que hace en la ciudad que encuentres en el mensaje. Si no encuantras una ciudad en el mensaje, devuelveme que no has encontrado una ciudad en el mensaje"}
]

user_imput = input("You: ")
messages.append({"role": "user", "content": user_imput})

completion = client.chat.completions.create(model="LLaMA_CPP", messages=messages)

response = completion.choices[0].message.content
print("AI: ", response)

messages.append({"role": "assistant", "content": response})
