class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, data):
        node = Node(data)
        if self.head is None:
            node.next = None
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insetAfterNode(self, after, data):
        node = Node(data)
        temp = self.head
        while temp.data != after:
            temp = temp.next
        node.next = temp.next
        node.prev = temp
        temp.next = node
        node.next.prev = node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


dll = DoublyLinkedList()
lst = [10, 20, 30, 40]
for l in lst:
    dll.insertAtBeg(l)
dll.traverse()
print()
dll.insetAfterNode(20, 25)
dll.traverse()
