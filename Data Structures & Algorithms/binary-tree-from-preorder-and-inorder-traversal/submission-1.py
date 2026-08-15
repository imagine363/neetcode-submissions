class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        pos = {}
        for i,value in enumerate(inorder):
            pos[value] = i

        pre_indx = 0

        def build(left,right):
            if left > right:
                return None
            
            nonlocal pre_indx
            root_val = preorder[pre_indx]
            pre_indx += 1
            mid = pos[root_val]

            root = TreeNode(root_val)
            root.left = build(left,mid-1)
            root.right = build(mid+1,right)

            return root
        return build(0,len(inorder)-1)