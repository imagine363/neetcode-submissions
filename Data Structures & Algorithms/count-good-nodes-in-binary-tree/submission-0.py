class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self,root,maxalltime):
        count = 0
        if root is None:
            return 0
        if root.val >= maxalltime:
            maxalltime = root.val
            count = 1
        goodl = self.traverse(root.left,maxalltime)
        goodr = self.traverse(root.right,maxalltime)
        return count + goodl + goodr
        
    def goodNodes(self, root: TreeNode) -> int:
        res = self.traverse(root,root.val)
        return res