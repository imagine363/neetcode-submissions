class Node:
    def __init__(self,key=None,value=0):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        nxt = node.next
        prev = node.prev

        prev.next = nxt
        nxt.prev = prev

        node.prev = None
        node.next = None

    def insert(self,node):
        beforelast = self.right.prev
        beforelast.next = node

        node.prev = beforelast
        node.next = self.right

        self.right.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        size = len(self.cache)
        if key not in self.cache:
            size += 1
            if size > self.capacity:
                firstnode = self.left.next
                self.remove(firstnode)
                del self.cache[firstnode.key]
            newnode = Node(key,value)
            self.cache[key] = newnode

            self.insert(newnode)
        else:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.insert(node)

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))    

cache.put(3, 3)

print(cache.get(2))   

cache.put(4, 4)

print(cache.get(1))    
print(cache.get(3))    
print(cache.get(4))    


#result should be 1 -1 3 4
