def add_everything_up(a, b):
    if type(a) == float and type(b) == int:
        return float(a) + float(b)
    else:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))