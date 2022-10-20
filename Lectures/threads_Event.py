from threading import Event, Thread
from time import sleep


e = Event()


def master(e):
    sleep(1)
    print('Set event...')
    e.set()


def slave(e, name):
    print(f'{name} waiting...')
    e.wait()
    print(f'{name} finished\n')


m = Thread(target=master, args=(e, ))
w2 = Thread(target=slave, args=(e, 'second'))
w1 = Thread(target=slave, args=(e, 'first'))

w1.start()
w2.start()
m.start()