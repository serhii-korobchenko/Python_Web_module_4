from threading import Thread
from time import sleep


class UsefulClass():
    def __init__(self, second_num):
        self.delay = second_num

    def __call__(self):
        sleep(self.delay)
        print('Wake up!')


t2 = UsefulClass(2)
thread = Thread(target=t2)
thread_locking = Thread(target=t2)

thread.start()
print(thread.is_alive(), thread_locking.is_alive())
thread_locking.start()
thread.join()
thread_locking.join()
print('After all...')