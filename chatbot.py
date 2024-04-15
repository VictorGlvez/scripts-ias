from openai import OpenAI


client1 = OpenAI(
    base_url="http://127.0.0.1:8081/v1",
    api_key = "sk-no-key-required")
    
client2 = OpenAI(
    base_url="http://127.0.0.1:8081/v1",
    api_key = "sk-no-key-required")

message1 = [
    {"role": "system", "content": "You are man who want to find love with a woman."}
]

message2 = [
    {"role": "system", "content": "You are woman who want to find love with a man."}
]

message1.append({"role": "user", "content": "Hello, im a woman, how are you"})



while(True):

    completion1 = client1.chat.completions.create(model="LLaMA_CPP", messages=message1)
    response1 = completion1.choices[0].message.content
    print("AI1: ", response1)
    message2.append({"role": "user", "content": response1})
    completion2 = client2.chat.completions.create(model="LLaMA_CPP", messages=message2)
    response2 = completion2.choices[0].message.content
    print("AI2: ", response2)
    message1.append({"role": "user", "content": response2})