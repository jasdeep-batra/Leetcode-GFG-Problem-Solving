# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head.next
        prev = head
        sum1 = 0 
        while(ptr.next):
            if ptr.next.val==0:
                sum1 += ptr.val
                ptr.val = sum1
                prev.next = ptr
                sum1 = 0
                prev = ptr.next
            else:
                sum1+=ptr.val
            ptr = ptr.next
        
        head = head.next;
        ptr2 = head
        while(ptr2.next.next):
            if ptr2.next.val==0:
                ptr2.next = ptr2.next.next
            ptr2 = ptr2.next
            
        ptr2.next = None


        return head




        