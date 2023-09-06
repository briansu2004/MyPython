ti = None

file_name = "/tmp/example.txt"

for i in range(10):
    with open(file_name, 'w') as ti:
        if (i > 6):
            break

print(ti.closed)
