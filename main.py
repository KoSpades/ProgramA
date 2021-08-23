import requests

r = requests.get('https://api.github.com/events')

response = r.json()

print(response)
