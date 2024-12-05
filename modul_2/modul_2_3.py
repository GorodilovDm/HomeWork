my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
position = 0
while position < len(my_list):
    if my_list[position] == 0:
        position += 1
        continue
    elif my_list[position] > 0:
        print(my_list[position])
        position += 1
    else:
        break
else:
    print('Нет отрицательных значений')