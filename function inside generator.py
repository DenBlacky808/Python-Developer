from math import sqrt

numbers = [-123, 81, 56, 44, 1, 9, 96, -18, -20, 48, 33, 51, 15]


def sqrt_positive(new_numbers):
    result = [sqrt(number) if number > 0 else number for number in new_numbers]
    return result


print(sqrt_positive(numbers))
print(numbers)
