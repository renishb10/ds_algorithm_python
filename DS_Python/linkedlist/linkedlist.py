class Node(object):

    #constructor in python
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # Complexity O(1)
    def insertAtStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        #check if list already has node (not empty) head is not empty
        if not self.head:
            self.head = newNode
        else: 
            newNode.nextNode = self.head
            self.head = newNode

    # Complexity O(N)
    def insertAtEnd(self, data):
        newNode = Node(data)
        currentNode = self.head
        self.size = self.size + 1
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        
        currentNode.nextNode = newNode

    # Complexity O(N)
    def remove(self, data):
        self.size = self.size - 1
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            print(currentNode.data)

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    # Complexity O(1)
    def getSize(self):
        return self.size

    # Complexity O(N)
    def getSizeByIterate(self):
        size = 0
        currentNode = self.head
        while currentNode is not None:
            size+=1
            currentNode = currentNode.nextNode
        return size

    # Complexity O(N)
    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

linkedList = LinkedList()

linkedList.insertAtStart(12)
linkedList.insertAtStart(122)
linkedList.insertAtStart(3)
linkedList.insertAtEnd(31)

linkedList.remove(3)
linkedList.printList()

