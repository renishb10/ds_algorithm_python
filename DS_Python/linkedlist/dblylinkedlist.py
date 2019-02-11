class Node(object):    
    def __init__(self, data):
        self.data = data
        self.prevNode = None
        self.nextNode = None

class DbyLinkedList(object):
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def insertAtStart(self, data):
        self.size += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head.prevNode = newNode

    def insertAtEnd(self, data):
        self.size += 1
        newNode = Node(data)
        if 