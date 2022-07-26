from itertools import product


def div_counter(n):
    dl = 2
    d = 2
    while d*d < n:
        if n % d == 0:
            dl += 2
        d += 1
    if d*d == n:
        dl += 1
    return dl


# 34887832
numbers = '0123456789'

for len in range(4):
    for asteric in product(numbers, repeat=len):
        for question in numbers:
            ast = ''.join(asteric)
            num = int('3'+ast+'8'+question)
            if int(num**0.5) == num**0.5 and div_counter(num) == 9:
                print(num, num**0.5)
