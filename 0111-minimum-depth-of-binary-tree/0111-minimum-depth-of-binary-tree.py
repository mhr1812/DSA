# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        depth = 1
        
        while queue:
            size = len(queue)
            
            for _ in range(size):
                removed = queue.popleft()
                
                if not removed:
                    continue
                
                if not removed.left and not removed.right:
                    return depth
                
                if removed.left:
                    queue.append(removed.left)
                
                if removed.right:
                    queue.append(removed.right)
            
            depth += 1
        
        return 0