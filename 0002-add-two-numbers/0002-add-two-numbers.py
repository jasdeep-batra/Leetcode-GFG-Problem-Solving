# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        itr1,itr2 = l1,l2
        temp = ListNode(-1,None)
        head = temp
        while itr1 and itr2:

            summ = itr1.val + itr2.val + carry
            itr1.val = (summ)%10
            temp.next = itr1
            temp = temp.next
            if (summ) <= 9:
                carry = 0
            else:
                print("work")
                carry = 1

            itr1 = itr1.next
            itr2 = itr2.next

        while itr1:
            summ = itr1.val + carry
            itr1.val = (summ)%10
            temp.next = itr1
            temp = temp.next
            if summ <= 9:
                carry = 0
            else:
                carry = 1
            itr1 = itr1.next
        while itr2:
            summ = itr2.val + carry
            itr2.val = (summ)%10
            temp.next = itr2
            temp = temp.next
            if (summ)>9:
                carry = 1
            else:
                carry = 0
            itr2=itr2.next
        if carry:
            temp.next = ListNode(1,None)
        return head.next
        