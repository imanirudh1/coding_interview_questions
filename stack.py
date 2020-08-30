class Stack(object):
    def __init__(self):
        self.item=[]

    def push(self,i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        return self.item == []  

    def size(self):
        return len(self.item)                  

a=Stack()
print("Stack is empty ",a.isEmpty())
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)
print(a.peek())
print('Delete last element ',a.pop())
print('Delete last element ',a.pop())
print("Length of the stack ",a.size())
print("Stack is empty ",a.isEmpty())