# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def gcd(self, num1, num2):
        # make num1 always smaller 
        if num1 > num2:
            num1,num2 = num2,num1
        ans = 1
        for i in range(1,num1+1):
            if num1%i==0 and num2%i==0:
                ans = max(ans,i)
        return ans
        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #math.gcd
        ptr1 = head
        ptr2 = head.next
        while ptr2:
            val1 = ptr1.val
            val2 = ptr2.val
            nval = self.gcd(val1,val2)
            ins = ListNode(nval,ptr2)
            ptr1.next = ins
            ptr1 = ptr2
            ptr2=ptr2.next
        return head


        