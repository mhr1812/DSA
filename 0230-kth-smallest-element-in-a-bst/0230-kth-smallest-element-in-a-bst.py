# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        def inorder(n):
            c = 0
            curr = n
            while curr or st:
                while curr:
                    st.append(curr)
                    curr = curr.left 
                curr = st.pop()
                c+=1
                if c==k:
                    return curr.val 
                curr = curr.right
        return inorder(root)