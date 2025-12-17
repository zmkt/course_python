from random import choice


def genPass(length: int, arrayel: str):
    res = ''
    for _ in range(length):
        res += choice(arrayel)

    return res


print(genPass(50, 'qwertyuQWERTY'))
