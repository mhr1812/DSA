# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node.left: 
                q.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)

            if node.right: 
                q.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

        q = collections.deque([(target, 0)])
        visited = set([target])
        ans = []
        while q:
            node, d = q.popleft()
            if d == k:
                ans.append(node.val)
                continue

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, d+1))

        return ans