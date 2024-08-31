# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return root
        if root.val==p.val or root.val==q.val:
            return root
        Left = self.lowestCommonAncestor(root.left,p,q)
        Right = self.lowestCommonAncestor(root.right,p,q)

        if Left and Right:
            return root
        return Left if Left else Right
        


        