# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
    
        if head.next == None:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotateTimes = k%length

        if k == 0 or rotateTimes == 0:
            return head

        fastPointer = head
        slowPointer = head

        for a in range (rotateTimes):
            fastPointer = fastPointer.next


        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        temp = slowPointer.next

        slowPointer.next = None
        fastPointer.next = head
        head = temp

        return head
