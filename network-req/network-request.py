import requests

response = requests.get("http://localhost:8082/add-user?username=zhangSan&password=123")

code = response.status_code
t = response.json()

print(t)

