import random
import string

# Function to generate random words
def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Specify the output file path
output_file_path = '/tmp/large_text_file.txt'

# Specify the desired file size in bytes (1GB)
file_size_bytes = 1024 * 1024 * 1024  # 1GB

# Specify the word length and separator
word_length = 10  # Adjust the word length as needed
separator = ' '   # You can use other separators if needed

# Open the file for writing
with open(output_file_path, 'w') as file:
    while file.tell() < file_size_bytes:
        word = generate_random_word(word_length)
        file.write(word)
        file.write(separator)

print(f"File '{output_file_path}' created with a size of 1GB.")
