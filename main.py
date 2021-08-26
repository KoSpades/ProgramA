import requests

# we don't want programA to send an intent on behalf of programB
# Intents probably also need to be signed

# The following link refers to the policy broker's URL

payload = {"subject": "programA", "object": "fileA", "action": "read"}

# Making a test request
# r_root = requests.get('http://127.0.0.1:8000/').json()
# print(r_root)

# Making a post request (posting the intent) to get a token
r_check = requests.post('http://127.0.0.1:8000/token', json=payload)
token_json = r_check.json()

# Note that after we get the token, we have to put in the right format as a string.
# This string will be used in the headers of our subsequent file access requests.
token_str = token_json["token_type"] + " " + token_json["access_token"]
# print(token_str)
# print(r_check.status_code)

# Making a get request to read file A
headers = {"Authorization": token_str}
r_file = requests.get('http://127.0.0.1:8000/fileA', headers=headers)
print(r_file.json())
print(r_file.status_code)



