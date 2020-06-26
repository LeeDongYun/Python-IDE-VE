import random

# 전역 변수 items
items = [1, 2, 3, 4, 5, 6, 7]
def myshuffle(lst):
    random.shuffle(lst)
    return lst

my = [myshuffle(items) for _ in range(5)]
print(my)

# 내부적으로 변화더라도 전역 변수인 마지막 값으로
items = [1, 2, 3, 4, 5, 6, 7]
def myshuffle2(lst):
    random.shuffle(lst)
    print(lst)
    return lst

my = [myshuffle2(items) for _ in range(5)]
print(my)

import random
items = [1, 2, 3, 4, 5, 6, 7]

# 내부적으로 새로운 값으로 복사해 반환
def myshuffle3(lst):
    random.shuffle(lst)
    print(lst)
    return lst.copy()

my = [myshuffle3(items) for _ in range(5)]
print(my)

