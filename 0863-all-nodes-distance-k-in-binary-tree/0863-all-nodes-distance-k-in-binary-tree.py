# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr.left:
                    parent[curr.left.val] = curr
                    q.append(curr.left)
                if curr.right:
                    parent[curr.right.val] = curr
                    q.append(curr.right)
        visited = {}
        q.append(target)
        while k>0 and q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                visited[curr.val] = 1
                if curr.left and curr.left.val not in visited:
                    q.append(curr.left)
                if curr.right and curr.right.val not in visited:
                    q.append(curr.right)
                if curr.val in parent and parent[curr.val].val not in visited:
                    q.append(parent[curr.val])
            k-=1 
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr.val)
        return ans