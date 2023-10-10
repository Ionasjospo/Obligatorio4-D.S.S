import requests
import json

url = 'http://localhost:8080/AltoroJ/api/login'
session = requests.Session()

username = input("Enter username\n")
password = input("Enter password\n")

payload = {
    "username": username,
    "password": password
}

headers = {
    'Content-Type': 'application/json'
}

response = session.post(url, json=payload, headers=headers)

try:
    response_json = response.json()
except json.JSONDecodeError:
    print("La respuesta no es un JSON válido")
    exit()

if 'error' in response_json:
    print(f"0, {response_json['error']}")
elif 'success' in response_json:
    print(f"1")
   # print(f"Token de autorización: {response_json['Authorization']}")
else:
    print("Respuesta inesperada")

