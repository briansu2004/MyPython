import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token_url = "..."

test_api_url = "..."

client_id = '<<client_id>>'
client_secret = '<<client_secret>>'

data = {'grant_type': 'client_credentials'}

access_token_response = requests.post(
    token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print(access_token_response.headers)
print(access_token_response.text)

tokens = json.loads(access_token_response.text)

print("access token: " + tokens['access_token'])

api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
# Same for POST etc.
api_call_response = requests.get(
    test_api_url, headers=api_call_headers, verify=False)

print(api_call_response.text)
