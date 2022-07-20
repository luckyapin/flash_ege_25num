
from itertools import product


# длина посл-ти в @ должна быть до 3 т.к. 5 цифр уже есть, а нам нужно меньше 9
for lenght in range(1, 5):

    # перебираем все последовательности для @
    for k in product('02468', repeat=lenght):

        for dollar in range(1, 10, 2):  # все нечетные

            at = ''.join(k)
            number = int('4'+at+'3'+str(dollar)+'79')
            if number % 73 == 0 and number < 10**8:
                print(number, number//73)
