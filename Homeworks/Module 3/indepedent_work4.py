def test(*par):
    print(par)

def func(a):
    if a <= 1:
        return 1
    else:
        return a * func(a - 1)
