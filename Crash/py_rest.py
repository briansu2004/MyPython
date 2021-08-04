import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
# >>>> Response < 200 >

# print(response.content())  # Return the raw bytes of the data payload
# print(response.text())  # Return a string representation of the data payload
# print(response.json())  # This method is convenient when the API returns JSON

query = {'lat': '45', 'lon': '180'}
response = requests.get(
    'http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())

# Create a new resource
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.json())

# Update an existing resource
response = requests.put('https://httpbin.org/put', data={'key': 'value'})
print(response.json())

print(response.headers["date"])


requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', 'password')
)

my_headers = {'Authorization': 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)

session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
response = session.get('https://httpbin.org/headers')


response = requests.get("http://api.open-notify.org/astros.json")
if response.status_code == 200:
    print("The request was a success!")
    # Code here will only run if the request is successful
elif response.status_code == 404:
    print("Result not found!")
    # Code here will react to failed requests


try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.


try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.TooManyRedirects as error:
    print(error)


response = requests.get(
    'http://api.open-notify.org/astros.json', max_redirects=2)

response = requests.get(
    'http://api.open-notify.org/astros.json', allow_redirects=False)


try:
    response = requests.get('http://api.open-notify.org/astros.json')
    # Code here will only run if the request is successful
except requests.ConnectionError as error:
    print(error)


try:
    response = requests.get(
        'http://api.open-notify.org/astros.json', timeout=0.00001)
    # Code here will only run if the request is successful
except requests.Timeout as error:
    print(error)


try:
    response = requests.get(
        'http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
