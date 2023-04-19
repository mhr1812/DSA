# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        a = [(root,0,None)]
        ans = 0
        while a:
            node,n,dir = a.pop()
            if node:
                ans= max(ans,n)
                a.append((node.left,1 if dir else n+1,1))
                a.append((node.right,n+1 if dir else 1,0))
        return ans