# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isequal(p,q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            if p.val!=q.val:
                return False
            return isequal(p.left,q.right) and isequal(p.right,q.left)

        return isequal(root.left, root.right)
                