class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    # least recently used cache size of capacity

    def __init__(self, capacity: int):
        # hashmap, each key -> linked list node (value)
        # right and left dummy node to keep track of rightmost, leftmost pos
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        previous = node.prev
        next = node.next
        previous.next = next
        next.prev = previous

    def insert(self, node):
        # insert to the left of right dummy
        previous = self.right.prev
        next = self.right
        node.next = self.right
        node.prev = previous
        previous.next = node
        self.right.prev = node
        

    def get(self, key: int) -> int:
        # return value if key exists, otherwise return -1
        # hashmap get for that key, return data stored in node
        # remove and reinsert to the right most
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # update value if key exists, otherwise add
        # if new pair over capcity, we remove least recently used
        # hashmap -> linked list, doubly since O(1)
        # functions
        # update key, update node data
        # if new key, we add key to hashmap, pair up with new node at end
        # check len of hashmap.values if exceed cap we remove left most (least)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # overwrites
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            


