# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = res = ListNode()

        curr1 = l1
        curr2 = l2

        carry = 0
        while curr1 and curr2:

            acc = curr1.val + curr2.val + carry
            
            sm = acc%10
            carry = acc//10
            
            
            res.next = ListNode()
            res = res.next
            res.val = sm
            
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            acc = curr1.val + carry
            sm = acc%10
            carry = acc//10

            res.next = ListNode()
            res = res.next
            res.val = sm

            curr1 = curr1.next

        while curr2:
            acc = curr2.val + carry
            sm = acc%10
            carry = acc//10

            res.next = ListNode()
            res = res.next
            res.val = sm

            curr2 = curr2.next

        if carry:
            res.next = ListNode()
            res = res.next
            res.val = carry


        return head.next

        