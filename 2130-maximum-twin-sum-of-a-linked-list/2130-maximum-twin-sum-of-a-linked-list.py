# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast,mid = head,head
        
        while fast:
            mid = mid.next
            fast = fast.next.next
            
        prev,curr = None,mid
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second = prev
        first = head 
        ans = 0
        while first and second:
            ans = max(ans,first.val+second.val)
            first = first.next 
            second = second.next
        return ans