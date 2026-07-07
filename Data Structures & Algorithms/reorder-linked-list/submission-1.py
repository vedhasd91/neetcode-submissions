# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find half

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        # reverse the second list
        prev = None

        while head2:
            tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = tmp

        head2 = prev
        
        # merge
        while head2:
            tmp1, tmp2 = head.next, head2.next
            head.next = head2
            head2.next = tmp1
            head, head2 = tmp1, tmp2

        