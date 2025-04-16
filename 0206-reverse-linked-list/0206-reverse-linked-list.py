# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        curr = head.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = None
        return prev




        