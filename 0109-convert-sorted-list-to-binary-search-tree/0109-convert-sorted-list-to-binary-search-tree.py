# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_mid(node):
            prev = None
            slow = node
            fast = node
            while fast and fast.next:
                prev = slow
                fast = fast.next.next
                slow = slow.next
            if prev:
                prev.next= None
            return slow
        def build(node):
            if not node:
                return None
            if not node.next:
                return TreeNode(node.val)
            mid = get_mid(node)
            root = TreeNode(mid.val)
            root.left = build(node)
            root.right = build(mid.next)
            return root

        return build(head)