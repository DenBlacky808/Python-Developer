numbers = [-123, 23, 56, 44, 15, 12, 96, -18, -20, 48, 33, 51, 150]
result = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0]
print(result)
