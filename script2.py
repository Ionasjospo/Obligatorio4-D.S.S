import requests
import sys

# Verifica si se proporcionan 3 args
if len(sys.argv) != 3:
    print("Para usar el programa debes introducir 3 argumentos: python3 script.py <host> <port>")
    sys.exit(1)


host = sys.argv[1]
port = sys.argv[2]

url = 'http://' + host + ':' + port + '/AltoroJ/search.jsp'

payload = "<script>alert('Cross Site Scripting')</script>"

params = {'query': payload}
response = requests.get(url, params=params)

if payload in response.text:
    exit_code = 1  # Existe vulnerabilidad
else:
    exit_code = 0  # No existe vulnerabilidad

print(f'Exit code: {exit_code}')