import random

i = 101
b = 0
answer = None
while True:
    Move = random.randint(b + 1, i - 1)
    print(f"Is this number {Move} ?")
    answer = input()
    if answer == '=':
        print('Yeah! I won!')
        break
    elif answer == '<':
        i = Move
    else:
        b = Move
