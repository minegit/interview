class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

def treeHt(root):
    if root == None:
        return 0
    q = []
    q.append(root)
    h = 0
    while True:
        nodeCount = len(q)
        if nodeCount == 0:
            return h
        h +=1
        while nodeCount > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodeCount-=1
    return h
def maxdepth(root):
    if root is None:
        return -1
    else:
        lh = maxdepth(root.left)
        rh = maxdepth(root.right)
        return max(lh+1, rh+1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)

print(treeHt(root))
print(maxdepth(root)+1)
