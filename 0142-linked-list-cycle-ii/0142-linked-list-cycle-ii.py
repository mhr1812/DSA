# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        f = 0
        while True:
            if fast==None:
                f = 1 
                break
            if fast.next==None:
                f = 1 
                break
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
        if f:
            return None
        else:
            slow = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            return slow