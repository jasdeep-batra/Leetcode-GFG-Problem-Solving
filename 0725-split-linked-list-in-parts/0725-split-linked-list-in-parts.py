# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if head == None:
            return [None]*k
        count = 0
        ptr = head
        while ptr:
            count+=1
            ptr = ptr.next

        res = []
        if k > count:
            prev = head
            curr = head.next
            res = [prev]
            while curr:
                res.append(curr)
                prev.next = None 
                prev = curr            
                curr = curr.next



            for _ in range(k-count):
                res.append(None)
            
        else:
            split = count//k
            rem = count%k
            
            curr_head = head
            j = 1
            for i in range(k):
                prev_head = ListNode(-1,curr_head)
                res.append(curr_head)
                real_range = split
                if rem>0:
                    real_range +=1
                rem-=1
                for j in range(real_range):
                    curr_head = curr_head.next
                    prev_head = prev_head.next

                prev_head.next = None

        return res




            