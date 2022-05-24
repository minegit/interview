class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

def lca(root, d1, d2):
    if root is None:
        return None
    if root.data == d1 or root.data == d2:
        return root
    left_lca = lca(root.left, d1, d2)
    right_lca = lca(root.right, d1, d2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca is not None else right_lca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print ("LCA(4,5) = ", lca(root, 4, 5).data)
print ("LCA(4,6) = ", lca(root, 4, 6).data)
print ("LCA(3,4) = ", lca(root, 3, 4).data)
print ("LCA(2,4) = ", lca(root, 2, 4).data)
