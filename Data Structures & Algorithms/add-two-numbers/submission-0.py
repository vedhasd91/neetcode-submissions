# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1:
            return l2
        
        if not l2:
            return l1

        
        carry = 0

        res = ListNode()
        prev = None
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sm = l1_val + l2_val + carry

            if sm//10:
                carry = sm//10
            else:
                carry = 0


            new_node = ListNode(val=sm%10)
            if prev:
                prev.next = new_node

            if res.next is None:
                res.next = new_node
            prev = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        
        return res.next

        