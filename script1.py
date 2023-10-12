import requests
import json
import sys

# Verifica si se proporcionan 3 args
if len(sys.argv) != 3:
    print("Para usar el programa debes introducir 3 argumentos: python3 script.py <host> <port>")
    sys.exit(1)


host = sys.argv[1]
port = sys.argv[2]

url = 'http://' + host + ':' + port + '/AltoroJ/api/login'
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

