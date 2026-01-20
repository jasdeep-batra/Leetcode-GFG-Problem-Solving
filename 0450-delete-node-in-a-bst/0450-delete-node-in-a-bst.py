# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None
        if key > node.val:
            node.right = self.deleteNode(node.right,key)
        elif key < node.val:
            node.left = self.deleteNode(node.left,key)

        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            # we will choose smallest left
            replace = node.right
            while replace.left:
                replace = replace.left

            node.val = replace.val

            node.right = self.deleteNode(node.right,replace.val)

        return node

            