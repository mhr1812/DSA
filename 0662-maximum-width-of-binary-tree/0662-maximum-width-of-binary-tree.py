# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,0)])
        width = 0
        while q:
            width = max(width,q[-1][1] - q[0][1])
            for _ in range(len(q)):
                node,w = q.popleft()
                if node.left:
                    q.append((node.left,2*w-1))
                if node.right:
                    q.append((node.right,2*w))
        return width+1
        