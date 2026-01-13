# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        counter =  count()
        for head in lists:
            if head:
                heapq.heappush(pq,(head.val,next(counter),head))

        dummy = ListNode(-1,None)
        ptr = dummy
        while pq:
            val,cnt,first = heapq.heappop(pq)
            ptr.next = first
            ptr = ptr.next
            if first.next is not None:
                heapq.heappush(pq,(first.next.val,next(counter),first.next))
            
        return dummy.next


        


        