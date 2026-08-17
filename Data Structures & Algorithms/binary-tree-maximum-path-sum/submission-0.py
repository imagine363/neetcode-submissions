class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        idealval = float('-inf')
        def findbest(root):
            if root is None:
                return 0
            left = findbest(root.left)
            right = findbest(root.right)

            left = max(0,left)
            right = max(0,right)

            nonlocal idealval 
            idealval = max(idealval,left + root.val + right)

            return root.val + max(left,right)
        findbest(root)
        return idealval


root = TreeNode(-10)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxPathSum(root))