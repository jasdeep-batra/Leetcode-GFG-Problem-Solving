# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def helper(r):
            if not r:
                return 0
            
            length = 1  + max(helper(r.left),helper(r.right))
            return length

        return helper(root)
        