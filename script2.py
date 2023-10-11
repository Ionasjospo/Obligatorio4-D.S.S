import requests

url = 'http://localhost:8080/AltoroJ/search.jsp'
payload = "<script>alert('Cross Site Scripting')</script>"

params = {'query': payload}
response = requests.get(url, params=params)

if payload in response.text:
    exit_code = 1  # Existe vulnerabilidad
else:
    exit_code = 0  # No existe vulnerabilidad

print(f'Exit code: {exit_code}')