import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

todo = {"userId": 1, "title": "Buy milk", "completed": False}

response = requests.post(url=api_url, data=todo)
response.json()