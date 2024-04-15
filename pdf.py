import requests
import PyPDF2
from openai import OpenAI

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

pdf_file_path = r'C:\Users\Victor\Desktop\a.pdf'
pdf_text = extract_text_from_pdf(pdf_file_path)
 
client = OpenAI(
         base_url="http://127.0.0.1:8081/v1",
         api_key = "sk-no-key-required")
 
messages = [
         {"role": "system", "content": "Asistente nutricional"},
         {"role": "user", "content": f"Quiero que me respondas a mis preguntas utilizando unicamente la informacion dada en {pdf_text}"}
     ]
     
print(pdf_text)
     

while(True):
    mensaje = input("You: ")
     
    messages.append({"role": "user", "content": mensaje})
     
    completion = client.chat.completions.create(model="LLaMA_CPP", messages=messages)
     
    response = completion.choices[0].message.content.strip()
    print(response)


# peticion = requests.get(f"https://api.weatherapi.com/v1/current.json?key=d459be6a25e34875a0c83327240804&q={response}&aqi=no")
# 
#     messages.append({"role": "user", "content": f"Quiero que me devuelvas en lenguaje natural únicamente la condición meteorológica de y la temperatura actual de {response} cuya informacion la tienes que extraer de {weather_data}"})
#     completion = client.chat.completions.create(model="LLaMA_CPP", messages=messages)
#     finalresponse = completion.choices[0].message.content
#     
#     print("AI: ", finalresponse)
# 
# else:
#     print("error en la peticion")
