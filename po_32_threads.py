import time
from threading import Thread, Lock

lock = Lock()

def measure(n):
    time.sleep(3) # симуляция задержки
    result = n * 10 # симуляция измерения
    # В этот блок кода нельзя одновременно заходить нескольким потокам
    lock.acquire()
    print(n, result)
    lock.release()
    return n, result

#  При заметной задержке измерения синхронный код неудовлетоврителен
# for n in range(1, 10):
#     print(n, measure(n)[1])

for n in range(1, 10):
    thread = Thread(target=measure, args=(n,))
    thread.start()
