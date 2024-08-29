#tiempo_de_performance

import time
import random

def for_loop(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

def list_comprehension(n):
    return [i for i in range(n)]

n = random.randint(1000, 12000000)

start = time.perf_counter()
_ = for_loop(n)
print("El tiempo de ejecución de for_loop es:", time.perf_counter() - start)

start = time.perf_counter()
_ = list_comprehension(n)
print("El tiempo de ejecución de list_comprehension es:", time.perf_counter() - start)
