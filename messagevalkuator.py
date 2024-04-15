from openai import OpenAI


client = OpenAI(
    base_url="http://127.0.0.1:8081/v1",
    api_key = "sk-no-key-required")

messages = [
    {"role": "system", "content":"Your only purpose is evaluate if the comment you recieve is possitive or negative."},
    {"role": "user", "content":"You have to determinate if the comment you recive is possitive or negative"}
]

while(True):
    user_imput = input("You: ")
    messages.append({"role": "user", "content": user_imput})

    completion = client.chat.completions.create(model="LLaMA_CPP", messages=messages)

    response = completion.choices[0].message.content
    print("AI: ", response)

    messages.append({"role": "assistant", "content": response})