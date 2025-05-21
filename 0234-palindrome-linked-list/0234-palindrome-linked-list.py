# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #reverse it and  then iterate and check if equals

        slow = head
        fast = head
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            count+=1
        
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        p2 = head
        while prev:
            if prev.val!=p2.val:
                return False
            prev= prev.next
            p2 = p2.next
        return True
        