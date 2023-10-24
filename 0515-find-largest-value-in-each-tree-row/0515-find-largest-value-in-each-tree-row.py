class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        max_value = []

        queue = [root]

        while any(queue):

            max_value.append(max(node.val for node in queue))
            queue = [child for node in queue for child in (node.left,node.right) if child]

        return max_value