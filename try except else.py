def bless_you(number):
    if number == 13:
        raise ValueError
    else:
        return number ** 2


num = int(input('Input number from 1 to 100 '))

try:
    result = bless_you(num)
except ValueError:
    print('Bless you!')
else:
    print(result)
