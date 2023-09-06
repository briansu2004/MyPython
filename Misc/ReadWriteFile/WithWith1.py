# Define the file name and the mode (in this case, 'w' for write)
file_name = "/tmp/example.txt"

# Open the file in write mode using the 'with' statement
with open(file_name, 'w') as file:
    # Write data to the file
    file.write("Hello, world!\n")
    file.write("This is a sample file created using 'with'.\n")

# File is automatically closed when the 'with' block is exited
