def count_calls():
    global calls
    calls += 1


def string_info(string_):
    count_calls()
    return len(string_), string_.upper(), string_.lower()


def is_contains(string_, str_list):
    count_calls()
    # for i in range(len(str_list)):
    #     str_list[i] = str_list[i].upper()
    str_list = [j.upper() for j in str_list]
    if string_.upper() in str_list:
        return True
    return False


calls = 0
print(string_info('Urban University'))
print(string_info('Домашняя работа'))
print(is_contains('ЧЕрез', ['Ехал', 'Грека', 'через', 'реку']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
