from dataclasses import dataclass


class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.root = None
    
def countNode(root):
    if root is None:
        return 0
    return 1 + countNode(root.left)+countNode(root.right)

def isComplete(root, index, numberOfNode):
    if root is None:
        return True
    if index >= numberOfNode:
        return False
    return isComplete(root.left, index*2+1, numberOfNode) and isComplete(root.right, index*2+2, numberOfNode)

def isHeap(root):
    if root is None:
        return True
    if (root.left and root.left.data > root.data) or (root.right and root.right.data > root.data):
        return False
    if root.left:
        leftCheck = isHeap(root.left)
    if root.right:
        rightCheck = isHeap(root.right)
    return leftCheck and rightCheck
    
def checkIfHeap(root):
    numberOfNodes = countNode(root)
    if isComplete(root, 0, numberOfNodes) and isHeap(root):
        return True
    return False