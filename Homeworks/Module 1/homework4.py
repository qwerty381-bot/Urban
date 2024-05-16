immutable_var = ([1,1], 5, 'mango', True)
print(immutable_var)
immutable_var[1] = 6
print(immutable_var) # Выдаст ошибку, так как нельзя изменять что-то, кроме списков внутри кортежа.

mutable_list = ['Django', 'Yoda', 'Batman']
mutable_list[2] = 'Joker'
print(mutable_list)