# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if low <=node.val <= high:
                self.sum+=node.val
            inorder(node.right)
            return

        inorder(root)
        return self.sum
