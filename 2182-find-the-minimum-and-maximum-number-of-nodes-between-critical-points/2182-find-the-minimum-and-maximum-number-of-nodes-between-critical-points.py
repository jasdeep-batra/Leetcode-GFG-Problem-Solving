# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        arr = []
        i = 1
        while curr.next:
            if ((curr.val > prev.val) and (curr.val > curr.next.val))  or ((curr.val < prev.val) and (curr.val < curr.next.val)):
                arr.append(i)           
            i+=1
            prev = curr
            curr = curr.next
        maxx = -1
        if len(arr)>1:
            maxx = arr[len(arr)-1] - arr[0]
        minn = sys.maxsize
        for j in range(1,len(arr)):
            minn = min(minn,arr[j]-arr[j-1])
        if minn==sys.maxsize:
            minn = -1
        return [minn,maxx]




        
        