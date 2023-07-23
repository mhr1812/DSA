# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0 or n<1:
            return []

        t=[[] for _ in range(n+1)]
        t[1]=[TreeNode(0)]

        for i in range(3,n+1):
            for j in range(1,i):
                leftTree=t[j]
                rightTree=t[i-1-j]

                for leftSubtree in leftTree:
                    for rightSubtree in rightTree:
                        root=TreeNode(0)
                        root.left=leftSubtree
                        root.right=rightSubtree
                        t[i].append(root)

        return t[n]        