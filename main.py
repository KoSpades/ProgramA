import requests

# we don't want programA to send an intent on behalf of programB
# Intents probably also need to be signed

# The following link refers to the policy broker's URL

payload = {"subject": "programA", "object": "fileA", "action": "read"}

# Making a test request
r_root = requests.get('http://127.0.0.1:8000/').json()
print(r_root)

# Making a post request (posting the intent) to get a token
r_check = requests.post('http://127.0.0.1:8000/token', json=payload)
print(r_check.json())
# print(r_check.status_code)

# Making a get request to read file A
r_file = requests.get('http://127.0.0.1:8000/fileA').json()
print(r_file)



