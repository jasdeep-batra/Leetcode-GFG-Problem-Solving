# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first option reverse it then remove nth item
        #turtle approach
        fast = ListNode(-1,head)
        slow = fast
        start = fast
        if not head.next:
            return None
        for j in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        print(fast.val)
        print(slow.val, slow.next.val)
        slow.next = slow.next.next

        # print(slow.next.val)
        return start.next
        