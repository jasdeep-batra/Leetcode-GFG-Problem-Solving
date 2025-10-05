# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            diameter[0] = max(diameter[0],lh+rh)
            print(diameter[0])          
            return 1 + max(lh,rh)
        h = height(root)
        return diameter[0]


        