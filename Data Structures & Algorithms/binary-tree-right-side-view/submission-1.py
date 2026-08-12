from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        res = []
        q = deque([root])
        while q:
            lvlsize = len(q)
            for i in range(lvlsize):
                x = q.popleft()
                if i == lvlsize-1:
                    res.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return res
                
                