from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root):
        if root is None:
            return ""
        res = []
        def traverse(root):
            if root:
                res.append(root.val)
                traverse(root.left)
                traverse(root.right)
            else:
                res.append('N')
        traverse(root)
        return ",".join(map(str,res))
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        if not data:
            return None
        data = deque(data.split(","))
        def traverse():
            value = data.popleft()
                    
            if value == 'N':
                return None 
    
            root = TreeNode(int(value))
            root.left = traverse()
            root.right = traverse()

            return root
        return traverse()
