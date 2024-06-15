def word_count(file_path):
    word_count_dict = {}

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        content = content.lower()

        for char in '-.,\n':
            content = content.replace(char, ' ')
        
        words = content.split()

        for word in words:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_count_dict

file_path = 'P1_data.txt'
print(word_count(file_path))