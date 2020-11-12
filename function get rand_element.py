import random


def ret_rand(numbers):
    if not numbers:
        return None
    else:
        return random.choice(numbers)
