import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon")

print(response.json())

print(response.json()["result"])
