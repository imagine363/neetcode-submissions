class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        hmap = {}
        def cloning(node):
            if node in hmap:
                return hmap[node]
            copy = Node(node.val)
            hmap[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(cloning(i))
            return copy
        return cloning(node) if node else None

