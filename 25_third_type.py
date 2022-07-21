def prime(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False  # нахождение простых делителей
        d += 1
    return True


def div(n):
    d = 2
    maxdiv = 0
    while d*d <= n:
        if n % d == 0:  # проверка на делимость
            if prime(d):
                maxdiv = max(maxdiv, d)  # нахождение максимума
            if prime(n//d):
                maxdiv = max(maxdiv, d)
        d += 1
    return maxdiv


for i in range(4856923, 4856993+1, 2):
    maxdiv = div(i)
    if maxdiv % 10 == 3:  # оканчивается ли на 3
        print(i, maxdiv)
