# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        if root.val==p.val or root.val==q.val:
            return root
        
        check_left = self.lowestCommonAncestor(root.left,p,q)
        check_right = self.lowestCommonAncestor(root.right,p,q)

        if check_left and check_right:
            return root
        return check_left if check_left else check_right



        