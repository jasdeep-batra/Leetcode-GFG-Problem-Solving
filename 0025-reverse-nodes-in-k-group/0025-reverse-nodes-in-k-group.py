# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node and count<k:
            node = node.next
            count+=1
            
        if count < k:
            return head

        prev = None
        curr = head
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i+=1
        head.next = self.reverseKGroup(curr,k)

        return prev

        

            

        
