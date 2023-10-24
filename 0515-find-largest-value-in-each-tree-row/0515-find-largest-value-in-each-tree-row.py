class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        while queue:
            n = len(queue)
            largest = float('-inf')
            for _ in range(n):
                cur = queue.popleft()
                largest = max(cur.val, largest)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(largest)
        
        return result