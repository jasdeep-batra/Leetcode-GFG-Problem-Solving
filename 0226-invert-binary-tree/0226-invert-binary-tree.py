# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #a problem of dfs
        def helper(node):
            #base case
            if not node:
                return None
            
            left = helper(node.left)
            right = helper(node.right)

            node.left = right
            node.right = left

            return node

        return helper(root)