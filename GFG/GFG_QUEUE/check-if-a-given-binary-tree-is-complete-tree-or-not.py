from itertools import count


class Node():
    def __init__(self, data) -> None:
        self.left = None
        self.data = data
        self.right = None
    
def isFullTree(root):
    if root is None:
        return True
    queue = []
    flag = False
    queue.append(root)
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp.left:
            if flag == True:
                return False
            queue.append(temp.left)
        else:
            flag = True
        if temp.right :
            if flag == True:
                return False
            queue.append(temp.right)
        else:
            flag = True
    return True


def countNodes(root):
    if root is None:
        return 0
    return 1 +countNodes(root.left)+countNodes(root.right)

def isFullTreeRecur(root, index, number_nodes):
    if root is None:
        return True
    if index >= number_nodes:
        return False
    return isFullTreeRecur(root.left, 2*index+1, number_nodes) and isFullTreeRecur(root.right, 2*index+2, number_nodes)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
# root.right.right = Node(7)
print(isFullTree(root))

number_nodes = countNodes(root)
print(isFullTreeRecur(root, 0, number_nodes))