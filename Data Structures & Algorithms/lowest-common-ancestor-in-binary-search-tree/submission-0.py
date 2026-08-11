class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.left.right = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(3)
q = TreeNode(8)

sol = Solution()
print(sol.lowestCommonAncestor(root,p,q))
