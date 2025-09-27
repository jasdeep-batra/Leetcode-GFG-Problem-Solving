# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i,head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq,(head.val,i,head))

        #create a final list 
        temp = ListNode(-1)
        head = temp
        while pq:
            val,ind,curr = heapq.heappop(pq)
            temp.next = curr
            temp = temp.next
            if curr.next:
                heapq.heappush(pq,(curr.next.val,ind,curr.next))
            
        return head.next
