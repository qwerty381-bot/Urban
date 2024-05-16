def find_pairs():
    n = int(input("Введите число от 3 до 20: "))

    if n < 3 or n > 20:
        print("Число не входит в диапазон от 3 до 20")
        return

    for i in range(1, n):
        for j in range(1, n):
            if i + j == n:
                set_ = {f'{i}{j}' for i in range(1, n)}
                set_list = list(set_)
                set_list.sort()
                print(set_list)



find_pairs()

