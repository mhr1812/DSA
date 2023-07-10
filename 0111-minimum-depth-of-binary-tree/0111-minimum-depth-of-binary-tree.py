# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def recur(root):
            if root is None:
                return 0
            if root.left==root.right==None:
                 return 1
            if root.left is None:
                return 1+recur(root.right)
            if root.right is None:
                return 1+recur(root.left)
            return 1+min(recur(root.left),recur(root.right))
        return recur(root)