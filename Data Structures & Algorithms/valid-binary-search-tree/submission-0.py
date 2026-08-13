class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check(self,root, leftb,rightb):
        if root is None:
            return True
        if not ((root.val > leftb) and (root.val < rightb)):
            return False
        
        resl = self.check(root.left,leftb,root.val)
    
        resr = self.check(root.right,root.val,rightb)
        
        return resl and resr
    def isValidBST(self, root):
        res = self.check(root,float('-inf'),float('inf'))
        return res