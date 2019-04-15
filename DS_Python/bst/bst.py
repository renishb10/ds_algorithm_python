class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        #1st check if root is empty then insert here
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    #(O(logN))
    def insertNode(self, data, node):
        #2nd compare data with root
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMin(self):
        if self.root:
            value = self.getMinNode(self.root)
            print(str(value.data))

    def getMinNode(self, node):
        if node.leftChild:
            return self.getMinNode(node.leftChild)

        return node

    def getMax(self):
        if self.root:
            value = self.getMaxNode(self.root)
            print(str(value.data))
    
    def getMaxNode(self, node):
        if node.rightChild:
            return self.getMaxNode(node.rightChild)

        return node

    def traversePreOrder(self, root):
        if root:
            print(str(root.data))
            self.traversePreOrder(root.leftChild)
            self.traversePreOrder(root.rightChild)

    def traverseInOrder(self, root):
        if root:
            self.traverseInOrder(root.leftChild)
            print(str(root.data))
            self.traverseInOrder(root.rightChild)
    
    def traversePostOrder(self, root):
        if root:
            self.traversePostOrder(root.leftChild)
            self.traversePostOrder(root.rightChild)
            print(str(root.data))

    def traverseLevelOrder(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)

        while(len(queue) > 0):
            print(queue[0].data)
            node = queue.pop(0)

            if (node.leftChild):
                queue.append(node.leftChild)

            if (node.rightChild):
                queue.append(node.rightChild)

    def delete(self, data, root):
        if not root:
            return
        
        if data < root.data:
            root.leftChild = self.delete(data, root.leftChild)
        elif data > root.data:
            root.rightChild = self.delete(data, root.rightChild)
        else:
            if not root.leftChild and not root.rightChild:
                print("Removing node {0}", data)
                temp = root
                del root
                return temp
            
            if not root.leftChild:
                temp = root.rightChild
                del root
                return temp
            elif not root.rightChild:
                temp = root.leftChild
                del root
                return temp
            else:
                maxLeft = self.getMaxNode(root.leftChild)
                root.data = maxLeft.data
                root.leftChild = self.delete(maxLeft.data, root.leftChild)
            

_bst = BST()
_bst.insert(20)
_bst.insert(10)
_bst.insert(7)
_bst.insert(11)
_bst.insert(25)
_bst.insert(14)
_bst.insert(6)
_bst.insert(8)

#_bst.getMin()
#_bst.getMax()

#_bst.traversePreOrder(_bst.root)
#_bst.traverseInOrder(_bst.root)
#_bst.traversePostOrder(_bst.root)
#_bst.traverseLevelOrder(_bst.root)

_bst.delete(10, _bst.root)
_bst.traverseInOrder(_bst.root)