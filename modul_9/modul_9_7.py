def is_prime(func):
    def wrapper(a, b, c):
        summ = func(a, b, c)
        is_prime_ = True
        for j in range(3, summ, 2):
            if summ % 2 == 0:
                is_prime_ = False
                break
            if summ % j == 0:
                is_prime_ = False
                break
        if is_prime_:
            print('Простое')
        else:
            print('Составное')
        return summ

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
