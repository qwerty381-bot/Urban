def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'a', encoding = 'utf-8') as file:
        for i, string in enumerate(strings):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(i, position)] = string
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result:
  print(elem)
