# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1,n2 = head, head
        # while p is not None:
        #     k-=1
        #     if n2!=None:
        #         n2 = n2.next
        #     if k==0:
        #         n1 = p
        #         n2 = head
        #     p = p.next
        for i in range(1,k):
            n1 = n1.next
        p = n1
        while p.next:
            n2 = n2.next
            p = p.next
        n1.val,n2.val = n2.val,n1.val
        return head