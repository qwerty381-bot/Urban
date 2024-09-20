def custom_write(file_name, strings):
    strings = []
    with open(file_name, 'a', encoding = 'utf-8') as file:
        for elem in strings:
            file.write(strings[elem] + '\n')
    return strings

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result:
  print(elem)
