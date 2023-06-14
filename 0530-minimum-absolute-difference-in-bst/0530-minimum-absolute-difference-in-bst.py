# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        ans = float('inf')
        
        def inorder(n):
            nonlocal prev,ans
            if n is None:
                return False
            inorder(n.left)
            if prev!=None:
                ans = min(ans,n.val-prev)
            prev = n.val
            inorder(n.right)
        
        inorder(root)
        return ans
            
        