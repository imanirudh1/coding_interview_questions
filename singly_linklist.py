class LinkedListNode(object):
    def __init__(self,value):
        self.value=value
        self.nextnode=None

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.nextnode = b
b.nextnode = c
print(a.value)
print(b.nextnode.value)