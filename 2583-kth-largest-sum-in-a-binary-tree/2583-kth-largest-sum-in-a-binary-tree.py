# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def height(root):
            if root.left== None and root.right==None:
                return 0
            l,r = 0,0
            if root.left!=None:
                l = height(root.left)
            if root.right!=None:
                r = height(root.right)
            return max(l,r) + 1
        
        def getlsum(node,level,lsum):
            if node==None:
                return
            lsum[level] += node.val
            getlsum(node.left,level+1,lsum)
            getlsum(node.right,level+1,lsum)
            
                
        levels = height(root)+1
        lsum = [0 for i in range(levels)]
        getlsum(root,0,lsum)
        lsum.sort()
        if k<=levels:
            return lsum[-k]
        else:
            return -1
        
        