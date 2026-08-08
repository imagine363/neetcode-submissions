class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self,root):
        if not root:
            return 0
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        self.diameter = max(self.diameter,leftheight + rightheight)
        return 1 + max(leftheight,rightheight)
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.height(root)
        return self.diameter
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()

print(solution.diameterOfBinaryTree(root))