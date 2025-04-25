# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-1,None)
        ans= prev
        ptr1,ptr2 = list1,list2
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                prev.next = ptr1
                ptr1 = ptr1.next
            elif ptr2.val <= ptr1.val:
                prev.next = ptr2
                ptr2 = ptr2.next
            prev = prev.next

        while ptr1:
            prev.next = ptr1
            ptr1 = ptr1.next
            prev = prev.next
        while ptr2:
            prev.next = ptr2
            ptr2 = ptr2.next
            prev = prev.next
        return ans.next




        