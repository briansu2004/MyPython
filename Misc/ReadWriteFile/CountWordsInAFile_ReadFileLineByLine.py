file_path = '/tmp/enwik9' # /example.txt' # # /large_text_file.txt'  # Replace with the actual file path

with open(file_path, 'r') as file:
    total_word_count = 0  # Initialize a counter for the total number of words

    for line in file:
        # Split each line into words using whitespace as the delimiter
        words = line.split()

        # Process each word in the line
        for word in words:
            # # Print each word
            # print(word)
            total_word_count += 1  # Increment the total word count

    print(f"Total words processed: {total_word_count}")
