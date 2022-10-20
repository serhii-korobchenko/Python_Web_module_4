from threading import Semaphore, Thread
from time import sleep


def slave(cond, name):
    cond.acquire()
    print(f'{name} Got semaphore')
    sleep(1)
    cond.release()
    print(f'{name} finished\n')


pool = Semaphore(2)
w1 = Thread(target=slave, args=(pool, 'first'))
w2 = Thread(target=slave, args=(pool, 'second'))
w3 = Thread(target=slave, args=(pool, 'third'))

w1.start()
w2.start()
w3.start()