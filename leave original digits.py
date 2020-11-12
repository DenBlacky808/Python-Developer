my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = [2, 2, 5, 12, 8, 2, 12]
my_list_3 = [2, 2, 5, 12, 8, 2, 12]
for item1 in range(0, len(my_list_1), 1):
    a = 0
    for item2 in range(0, len(my_list_1), 1):
        if my_list_2[item2] == my_list_1[item1]:
            a += 1
            if my_list_2[item1] in my_list_3 and a >= 2:
                my_list_3.remove(my_list_2[item1])
print(my_list_3)
