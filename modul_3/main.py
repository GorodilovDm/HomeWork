# global_var = 'Я глобальная переменная'
#
# def local_scope():
#     global_var = '12345'
#     local_var = 'Локальная переменная'
#     print(f'Внутри функции: {local_var}')
#     print(f'Внутри функции: {global_var}')
#
# local_scope()
# try:
#     print(local_var)
# except NameError as e:
#     print(f'error: {e}')

def outer_func():
    outer_var = 'я переменная внешней функции'

    def inner_func():
        inner_var = 'я переменная внутренней функции'
        print(f'внутри внутренней функции :{inner_var}')
        print(f'внутри внутренней функции :{outer_var}')

    inner_func()
    print(f'внутри внешней функции {outer_var}')

    try:
        print(inner_var)
    except NameError as e:
        print(f'error {e}')

outer_func()