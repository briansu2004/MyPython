import json
import os

print(os.getcwd())  # prints the current working directory

# Load the JSON file
with open('ForWork/myrequest.json') as f:
    data = json.load(f)

# Access the value of the "Data" key
data_list = data['MyRequest']['Data']

# Print the list of "Data" values
print(data_list)
