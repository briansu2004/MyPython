import json
import os

# Get the full path of the JSON file
filename = os.path.join(os.getcwd(), 'ForWork', 'myrequest.json')

try:
    # Load the JSON file
    with open(filename) as f:
        data = json.load(f)

    # Access the value of the "Data" key
    data_list = data['MyRequest']['Data']

    # Print the list of "Data" values
    print(data_list)

except FileNotFoundError:
    print(f"Error: file {filename} not found.")

except KeyError:
    print(f"Error: 'MyRequest' field or 'Data' field not found in {filename}.")
