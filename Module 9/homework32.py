def sum_three(a, b, c):
    return a + b + c
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if type(result) == int:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)