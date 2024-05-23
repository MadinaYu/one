from timeit import default_timer as timer
from random import randint
start_time = timer()
N = 100
a = []
for i in range(N):
    a.append(randint(1, 9999))
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(f"Время: {timer() - start_time} сек.")
