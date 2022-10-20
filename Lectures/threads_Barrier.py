from threading import Barrier, Thread
from time import sleep

counter = 0


def slave(cond, name):
    print(f'{name} Come to barrier')
    cond.wait()
    global counter
    counter += 1
    print(f'{name} finished\n')


pool = Barrier(3)

w1 = Thread(target=slave, args=(pool, 'first'))
w2 = Thread(target=slave, args=(pool, 'second'))
w3 = Thread(target=slave, args=(pool, 'third'))

w1.start()
w2.start()
sleep(1)
w3.start()

w1.join()
w2.join()
w3.join()
print(counter)