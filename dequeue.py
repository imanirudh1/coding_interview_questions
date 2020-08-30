class Dequeue(object):
    def __init__(self):
        self.item=[]

    def addFront(self,i):
        self.item.append(i)

    def addBack(self,i):
        self.item.insert(0,i)

    def removeFront(self):
        return self.item.pop()

    def removeBack(self):
        return self.item.pop(0)    

    def isEmpty(self):
        return self.item == []  

    def size(self):
        return len(self.item)                  

a=Dequeue()
print("Dequeue is empty ",a.isEmpty())
a.addFront(1)
a.addFront(2)
a.addFront(3)
a.addBack(4)
a.addBack(5)
a.addBack(6)
print('Delete Front element ',a.removeFront())
print('Delete Rear element ',a.removeBack())
print("Length of the Dequeue ",a.size())
print("Dequeue is empty ",a.isEmpty())