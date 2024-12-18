info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_positions = {}
    i = 1
    file = open(file_name, 'w', encoding='utf8')
    for string in strings:
        strings_positions[i, file.tell()] = string
        file.write(string + '\n')
        i += 1
    file.close()
    return strings_positions


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
