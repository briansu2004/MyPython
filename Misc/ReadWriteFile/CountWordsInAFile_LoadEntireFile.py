import os

# Specify the path to the folder and the file name
folder_path = "c:\\tmp"
file_name = "example.txt"

# Combine the folder path and file name to get the full file path
file_path = os.path.join(folder_path, file_name)
# print(file_path)

# Check if the file exists
if os.path.isfile(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()

        # Split the content into words using whitespace as a delimiter
        words = file_content.split()

        # Count the number of words
        num_words = len(words)

        # Print the result
        print(f"The file '{file_name}' contains {num_words} words.")
else:
    print(f"The file '{file_name}' does not exist in the folder '{folder_path}'.")
