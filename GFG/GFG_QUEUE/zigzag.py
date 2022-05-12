from dataclasses import dataclass


class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left= None
def add(listQ, data):
    for x in listQ:
        data.append(x.data)
    return data

def zigzag(root):
    if root is None:
        print("  ", end=" ")
    q = []
    q2 = []
    currentDirL2R = False
    q.append(root)
    q2.append(root.data)
    q.append(currentDirL2R)
    while len(q)>=1:
        t = q.pop(0)
        if len(q)==0:
            continue
        if t == None:
            continue
        if  t == True or t == False:
            if t == False:
                q.reverse()
                q2 = add(q, q2)
                q.reverse()
            else:
                q2 = add(q, q2)
            q.append(not t)
        else:
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
    print(q2)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
zigzag(root)


