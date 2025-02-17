class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self, *args):
        super().__init__(*args)


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if len(self.__queue) == 0:
            raise (QueueError)
        return self.__queue.pop(0)

    def get_queue(self):
        return self.__queue


class SuperQueue(Queue):
    def __init__(self):
        super().__init__()

    def is_empty(self):
        return len(super().get_queue()) == 0


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

print("\n\n")

que2 = SuperQueue()
que2.put(1)
que2.put("dog")
que2.put(False)

for i in range(4):
    if not que2.is_empty():
        print(que2.get())
    else:
        print("Queue empty")
