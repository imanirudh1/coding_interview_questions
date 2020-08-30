class Queue(object):
    def __init__(self):
        self.item=[]

    def enqueue(self,i):
        self.item.insert(0,i)

    def dequeue(self):
        return self.item.pop()

    def isEmpty(self):
        return self.item == []  

    def size(self):
        return len(self.item)                  

a=Queue()
print("Queue is empty ",a.isEmpty())
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
a.enqueue(6)
print('Delete last element ',a.dequeue())
print('Delete last element ',a.dequeue())
print("Length of the Queue ",a.size())
print("Queue is empty ",a.isEmpty())