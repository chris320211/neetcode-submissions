# initialize the class so __init__ method
# get(self, key)
# return the value correspond to key if it exists
# move it to most recently used or right most
# put(self, key, value)
# update the value corresponding to the key if it exists
# if not we add to cache
# if capacity exceeds we remove left most
# key, value pair
# O(1), get, we have hashmap, we aslo need to move to front
# hashmap we cant keep track of what recently
# linked list because we need to keep track of order, O(N) lookup
# hashmap key -> node O(1) lookup
# we need to store both key, val in node
# remove when overcapacity, remove node, unlink from hashmap, we need the key stored int he node

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.front = Node(0,0)
        self.back = Node(0,0)
        self.front.prev = self.back
        self.back.next = self.front

    def insert(self, node):
        prev = self.front.prev
        next = self.front
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node
        
    def remove(self, node):
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.back.next
            self.remove(lru)
            del self.cache[lru.key]
        

    