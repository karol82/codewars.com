
import time
from math import sqrt
num = 53069


def is_prime(num):
    if num < 2: return False
    i = 2
    pierw = sqrt(num)
    while i <= pierw:
        print("num:", num, "i:", i, "pierw:", pierw)
        if num % i == 0:
            return False
        i += 1
    return True


t0 = time.time()
print(is_prime(num))
t1 = time.time()
print(t1-t0)