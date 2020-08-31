class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_last_node(n,head):
    left_node=head
    right_node=head
    for i in range(n-1):
        if not right_node.nextnode:
            raise LookupError("Error : n is larger than linked list.")
        else:
            right_node=right_node.nextnode
    while right_node.nextnode:
        left_node=left_node.nextnode
        right_node=right_node.nextnode
    return left_node.value            

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print(nth_last_node(2,a))