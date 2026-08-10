class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def sameTree(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        elif (root1 is None and root2 is not None) or (root1 is not None and root2 is  None):
            return False
        if root1.val != root2.val:
            return False
        if root1.val == root2.val and root1 and root2:
            resl = self.sameTree(root1.left,root2.left)
            resr = self.sameTree(root1.right,root2.right)
        return resl and resr
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if self.sameTree(root,subRoot):
            return True
        
        resl = self.isSubtree(root.left,subRoot)
        resr = self.isSubtree(root.right,subRoot)
        return resl or resr
        

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)