from threading import Thread
from queue import Queue


class SimpleThread(Thread):

    def __init__(self, thread_name, queue):

        super().__init__()
        self.thread_name = thread_name
        self.queue = queue

    def run(self):
        element = self.queue.get()
        print(f'{self.thread_name} got {element}')
        self.queue.task_done()

queue = Queue()

for i in range(10):
    queue.put(i)

print(queue.queue)

for i in range(5):
    SimpleThread(i, queue).start()
    print()
    print(queue.queue)



