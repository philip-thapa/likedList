class Node:
    def __init__(self, data):
        self.data = data
        self. next = None


class LikedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertAtLast(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def insertInBetween(self, prevNode, data):
        node = Node(data)
        temp = self.head
        while temp.data != prevNode:
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def traversal(self):
        if self.head is None:
            print("Liked list is empty", end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def deleteFirstNode(self):
        if self.head is None:
            print("Empty linked list")
        else:
            self.head = self.head.next

    def deleteBetweenNode(self, nodeToBeDeleted):
        temp = self.head
        while temp.next.data != nodeToBeDeleted:
            temp = temp.next
        temp.next = temp.next.next


list = LikedList()
l = [30, 50, 30, 60, 70]
for i in l:
    list.insertAtBegining(i)
list.traversal()
# list.insertAtLast(100)
# list.insertInBetween(50, 40)
# list.deleteFirstNode()
list.deleteBetweenNode(30)
print()
list.traversal()
