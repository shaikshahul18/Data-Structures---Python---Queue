class Queue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def isEmpty(self):
        return bool(self.queue == [])
    
    def peek(self):
        return self.queue[0]
    
    def sizeofQueue(self):
        return len(self.queue)
    
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.sizeofQueue())
print(queue.dequeue())