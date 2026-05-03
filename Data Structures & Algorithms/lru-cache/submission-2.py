# LRU cache size stores ints of size capcity
# we need constructor method
# get returns corresponding value to key if exists, otherwise -1
# get run O(1), hashamp for key value, already O(1)
# put updates the value of key if it exists to the value, otherwise it adds
# get run O(1), if capacity is reached we remove the least recently used
# we need to keep track of least recently used and most
# when operation called -> key value moves to right
# linked loist to keep track of order
# hashmap for O(1) lookup and updates
# doublylinkedlist so we can add and remove in O(1)
# tail and head node to keep track of left and rightmost

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.back = Node(0,0)
        self.front = Node(0,0)
        self.back.next = self.front
        self.front.prev = self.back

    def insert(self, node): 
        # should insert a right at all times
        # Node <=> FRONT, rehook it to Node <=> inseted <=> FRONT
        prev = self.front.prev
        node.next = self.front
        self.front.prev = node
        node.prev = prev
        prev.next = node

    def remove(self, node):
        # remove at any node
        # O = Node = O
        # break the links and link to next and prev O=O
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
        # remove node method
        # insert to right method

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
            # remove that node, we can take care of moving to right in both cases
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # unhook the last node
            lru = self.back.next
            self.remove(lru)
            del self.cache[lru.key]
        
        

    