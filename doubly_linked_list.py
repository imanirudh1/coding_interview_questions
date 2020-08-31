class DoublyLinkedList(object):
    def __init__(self,value):
        self.value=value
        self.next_node=None
        self.prev_node=None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

b.prev_node=a
b.next_node=c
a.next_node=b
c.prev_node=b
print(b.prev_node.value)
print(a.next_node.value)