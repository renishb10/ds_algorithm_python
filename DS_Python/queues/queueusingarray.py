class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

queue = Queue()
print(queue.sizeQueue())
print(queue.enqueue(35))
print(queue.enqueue(45))
print(queue.enqueue(55))
print(queue.peek())
print(queue.dequeue())
print(queue.peek())