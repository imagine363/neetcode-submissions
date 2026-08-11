from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        q = deque([root])
        x = 0
        while q:
            sizeoflvl = len(q)
            curlevel = []
            for _ in range(sizeoflvl): 
                x = q.popleft()
                curlevel.append(x.val)
                if x.left is not None:
                    q.append(x.left)
                if x.right is not None:
                    q.append(x.right)
            res.append(curlevel)
        return res
            
            

        
        