def wordCount(t):
    word_dict = {}

    # Read data from the file and process each line
    with open(t, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                # Remove punctuation and convert to lowercase for consistent counting
                word = word.strip('.,!?;:()[]{}\'"').lower()
                if word not in word_dict:
                    word_dict[word] = [line_number]
                elif line_number not in word_dict[word]:
                    word_dict[word].append(line_number)

    return word_dict

# Example usage:
result = wordCount('text_file.txt')  # Pass the filename containing text data
print(result)