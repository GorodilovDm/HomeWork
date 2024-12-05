import random

one_rnd = random.randint(3, 20)
result = []
for i in range(1, one_rnd):
    for j in range(1 + i, one_rnd):
        if one_rnd % (i + j) == 0:
            result.append(i)
            result.append(j)
print(f'{one_rnd} - число из первой вставки')
print(*result, ' - нужный пароль', sep='')
