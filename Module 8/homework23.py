import math
def add_everything_up(a, b):
   try:
       a = 123.456
       b = 'строка'
       print(a + b)

   except:
       print(str(a) + b)

   try:
       a = 'яблоко'
       b = 4215
       print(a + b)

   except:
       print(a + str(b))

   try:
       a = 123.456
       b = 7
       print(a + b)

   except:
       c = a + b
       print(round(c, 3))


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))