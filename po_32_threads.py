import time
from threading import Thread, Lock

lock = Lock()
results = []

def measure(n):
    if n != 5:
        time.sleep(3) # симуляция задержки
    else:
        time.sleep(30)
    result = n * 10 # симуляция измерения
    return n, result

def measure_wrapper(n):
    result = measure(n)
    # В этот блок кода нельзя одновременно заходить нескольким потокам:
    lock.acquire()
    # print(result)
    results.append(result)
    lock.release()

#  При заметной задержке измерения синхронный код неудовлетоврителен
# for n in range(1, 10):
#     print(n, measure(n)[1])

pool = []
for n in range(1, 10):
    # thread = Thread(target=measure, args=(n,))
    thread = Thread(target=measure_wrapper, args=(n,))
    thread.daemon = True
    pool.append(thread)
    thread.start()

# time.sleep(3.5)

# while len(results) < 9:
#     time.sleep(0.1)

# counter = 0
# while counter < 9:
#     time.sleep(0.1)
#     lock.acquire()
#     counter = len(results)
#     lock.release()

n = 1
for thread in pool:
    thread.join(5)
    if thread.is_alive():
        print(f"Данные с датчика {n} не получены")
    n += 1

results.sort()
print(results)
