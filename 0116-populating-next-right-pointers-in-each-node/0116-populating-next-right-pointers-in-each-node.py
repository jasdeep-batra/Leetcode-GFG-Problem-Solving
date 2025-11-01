"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = [root]
        if not root:
            return root
        while q:
            l = len(q)
            prev = None
            for i in range(l):
                curr = q.pop(0)
                if prev==None:
                    prev = curr
                else:
                    prev.next = curr
                    prev = curr
                left = curr.left
                right = curr.right
                if left:
                    q.append(left)
                if right:
                    q.append(right)
        return root



            
