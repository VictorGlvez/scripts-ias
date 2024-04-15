import requests
from openai import OpenAI

city = input("ciudad: ")

response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=d459be6a25e34875a0c83327240804&q={city}&aqi=no")

if response.status_code == 200:
    weather_data = response.json()
    condition = weather_data['current']['condition']['text']
    temperature = weather_data['current']['temp_c']
    print(condition)
    print(temperature)

    client = OpenAI(
        base_url="http://127.0.0.1:8081/v1",
        api_key = "sk-no-key-required")
 
    messages = [
        {"role": "system", "content": "Eres un maestro en la climatología"},
        {"role": "user", "content": f"Quiero que me devuelvas en lenguaje natural únicamente la condición meteorológica de {city}, la cual es: {condition}, y la temperatura actual, la cual es: {temperature} grados centígrados."}
    ]
 
 
    completion = client.chat.completions.create(model="LLaMA_CPP", messages=messages)
 
    response = completion.choices[0].message.content
    print("AI: ", response)

else:
    print("hubo un error con los datos del clima")