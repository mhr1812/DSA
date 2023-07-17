# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr.next = prev
        return curr
    
    def addTwoNumbers_simple(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret_list = ListNode()
        curr = ret_list
        carry: bool = False
        mid_sum: int
        while carry or l1 or l2:
            curr.next = ListNode()
            curr = curr.next
            mid_sum = 0
            if l1:
                mid_sum += l1.val
                l1 = l1.next
            if l2:
                mid_sum += l2.val
                l2 = l2.next
            if carry:
                mid_sum += 1
            carry = (mid_sum > 9)
            curr.val = mid_sum%10
        curr.next = None

        return ret_list.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        return self.reverseList(self.addTwoNumbers_simple(l1,l2))

