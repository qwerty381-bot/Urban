my_list = ['apple', 'coconut', 'watermelon', 'potato', 'cucumber', 'carrot']
print(f'List: {my_list}')
print(f'First element: {my_list[0]}')
print(f'Last element: {my_list[-1]}')
print(f'Sublist: {my_list[2:5]}')
my_list[2] = 'tomato'
print(f'Modified list: {my_list}')

my_dict = {'Targaryens': 'Daenerys Targaryen', 'Lannisters': 'Tywin Lannister', 'Starkey': 'Eddard Stark'}
print(f'Dictionary: {my_dict}')
print(f'The head of the house: {my_dict['Targaryens']}')
my_dict['Lannisters'] = 'Cersei Lannister'
my_dict['Greyjoys'] = 'Balon Greyjoy'
print(f'Modified dictionary: {my_dict}')