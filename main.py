import requests


# The following link refers to the policy broker's URL

payload = {"subject": "programA", "object": "fileA", "action": "read"}

r_root = requests.get('http://127.0.0.1:8000/').json()
print(r_root)

r = requests.post('http://127.0.0.1:8000/check', json=payload)
print(r.json())
