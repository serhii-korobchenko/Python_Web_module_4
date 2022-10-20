from threading import Condition, Thread
from time import sleep


def master(cond, delay):
    cond.acquire()
    print('Master locked...')
    sleep(delay)
    cond.notify_all()
    print('Notified all')
    cond.release()

def slave(cond, name):
    print('Waiting... ', name)
    cond.acquire()
    print(name, 'Got condition')
    cond.wait()
    print(name)
    cond.release()

c = Condition()
m = Thread(target=master, args=(c, 2))
w1 = Thread(target=slave, args=(c, 'first'))
w2 = Thread(target=slave, args=(c, 'second'))

w1.start()
w2.start()
sleep(1)
m.start()