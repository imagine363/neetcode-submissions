class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        kth = 0
        def helper(root):
            if root is None:
                return None
            
            left = helper(root.left)
            if left is not None:
                return left
            
            nonlocal kth
            kth += 1

            if kth == k:
                return root.val
            
            right = helper(root.right)
            if right is not None:
                return right

        return helper(root)
        
