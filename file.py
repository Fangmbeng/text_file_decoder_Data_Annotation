def decode(text_file_path: str) -> str:
    # Read file content
    with open(text_file_path, 'r') as file:
        lines = file.readlines()

    # Create a dictionary to easily access values
    word_dict = {int(line.split()[0]): line.split()[1] for line in lines}

    # Create a list of sorted keys
    sorted_keys = [key for key in sorted(word_dict.keys())]

    end_numbers_of_pyramid = []
    index = 0
    diff = 2

    while index < len(sorted_keys):
        end_numbers_of_pyramid.append(sorted_keys[index])
        index += diff
        diff += 1

    return ' '.join(word_dict[x] for x in end_numbers_of_pyramid)

# Example usage
message_file_path = './file.txt'
result = decode(message_file_path)
print(result)
