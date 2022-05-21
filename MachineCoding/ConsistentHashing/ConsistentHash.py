from bisect import bisect, bisect_left, bisect_right
import hashlib

from StorageNode import StorageNode


def hash_fn(key, total_slots):
    hsh = hashlib.sha256()
    hsh.update(bytes(key.encode("utf-8")))
    return int(hsh.hexdigest(), 16) % total_slots
# FOR easy testing purpose. Is not used.
def hash_fn1(key, total_slots):
    ordi = ord(key)
    return ordi % total_slots
class ConsistentHash():
    def __init__(self, total_slots=50) -> None:
        self._keys = []
        self.nodes = []
        self.total_slots = total_slots
    
    def add_node(self, node):
        rebalance_items = None
        if len(self._keys) >= self.total_slots:
            raise Exception("HALF SLOTS ARE FULL")
        key = hash_fn(node.host, self.total_slots)
        index = bisect(self._keys, key)
        if index > 0 and self._keys[index-1] == key:
            raise Exception("COLLISION DETECTED...")
        if self.nodes:
            if index == len(self.nodes):
                rebalance_items = self.nodes[0].storage
                self.nodes[0].storage = []
            else:
                rebalance_items = self.nodes[index].storage
                self.nodes[index].storage = []
        node.key = key
        self.nodes.insert(index, node)
        self._keys.insert(index, key)
        if rebalance_items:
            for item in rebalance_items:
                self.assign(item[0])
        print("node added" , node)
        return key

    def remove_node(self, node):
        if len(self._keys) == 0:
            raise Exception("hash space is empty")
        key = hash_fn(node.host, self.total_slots)
        # we find the index where the key would reside in the keys
        index = bisect_left(self._keys, key)

        # if key does not exist in the array we raise Exception
        if index >= len(self._keys) or self._keys[index] != key:
            raise Exception("node does not exist")

        # now that all sanity checks are done we popping the
        # keys and nodes at the index and thus removing presence of the node.
        items = self.nodes[index].get_storage()
        self._keys.pop(index)
        self.nodes.pop(index)
        print("Node removed : ", node)
        for item in items:
            self.assign(item[0])
        return key
    
    def get_assigned_node(self, item):
        key = hash_fn(item, self.total_slots)
        index = bisect_right(self._keys, key) % len(self._keys)
        node = self.nodes[index].fetch_file(item)
        return node
    
    def assign(self, item: str) -> str:
        """Given an item, the function returns the node it is associated with.
        """
        key = hash_fn(item, self.total_slots)

        # we find the first node to the right of this key
        # if bisect_right returns index which is out of bounds then
        # we circle back to the first in the array in a circular fashion.
        index = bisect_right(self._keys, key) % len(self._keys)
        self.nodes[index].put_file((item,key))
        # return the node present at the index
        return self.nodes[index]
    
    def print_node(self):
        for node in self.nodes:
            print(node)
ch = ConsistentHash(100)
x = 0
ch.add_node(StorageNode(name='E', host='5'))
for file in ["1", "2"]:
    name  = ch.assign(file).name
    if x == 1:
        print(f"file {file} (shown in green) resides on node {name}")
ch.print_node()
ch.add_node(StorageNode(name='B', host='2'))
ch.add_node(StorageNode(name='C', host='3'))
ch.remove_node(StorageNode(name='B', host='2'))
ch.print_node()
ch.add_node(StorageNode(name='B', host='2'))
ch.assign("A")
ch.print_node()
ch.get_assigned_node('A')
