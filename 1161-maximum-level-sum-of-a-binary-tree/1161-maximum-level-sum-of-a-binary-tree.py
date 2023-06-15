# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        ans,mx,level,sm = 0,-float('inf'),0,0
        q.append(root)
        
        while q:
            n = len(q)
            sm = 0
            for i in range(n):
                curr = q.popleft()
                sm+=curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            level+=1
            if mx<sm:
                mx = sm
                ans = level 
        return ans
                