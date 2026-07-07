# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        
        node.next ->  node1.next -> node2.next -> None

        rnode = head     
        """


        prev = None
        curr = None

        while head is not None:
            print(head.val, head.next)

            next_node = head.next

            curr = head
            curr.next = prev

            head = next_node
            prev = curr
            
        head = curr
        return head
