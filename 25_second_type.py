from itertools import product

numbers = '0123456789'
arr = []  # массив в котором будут уникальные суммы

for len1 in range(2):
    for asteric1 in product(numbers, repeat=len1):
        for question in numbers:
            ast1 = ''.join(asteric1)
            num1 = int('1234'+ast1+'5'+question+'6')

            for len2 in range(2):
                for asteric2 in product(numbers, repeat=len2):
                    for question in numbers:
                        ast2 = ''.join(asteric2)
                        num2 = int('687'+ast2+'6'+question+'54')

                        final = num1+num2
                        if final % 4876 == 0:
                            if final not in arr:
                                arr.append(final)

arr.sort()
for i in arr:
    print(i, i//4876)
