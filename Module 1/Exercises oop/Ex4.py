class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.capacity
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)
    
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("enqueue to full queue")
        self.queue.append(value)
    
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[0]

queue1 = Queue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())  # False

print(queue1.front())  # 1

print(queue1.dequeue())  # 1

print(queue1.front())  # 2

print(queue1.dequeue())  # 2

print(queue1.is_empty())  # True
