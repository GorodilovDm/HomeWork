from itertools import combinations


def all_variants(text):
    for n in range(len(text)):
        f = combinations(text, n + 1)
        for x in f:
            yield ''.join(x)


a = all_variants("abcd")
for i in a:
    print(i)
