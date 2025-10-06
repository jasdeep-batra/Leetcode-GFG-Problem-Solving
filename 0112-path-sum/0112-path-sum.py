# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        #either dfs or bfs
        q = [(root,root.val)]
        while q:
            for i in range(len(q)):
                curr,summ = q.pop(0)
                if not curr.left and not curr.right:
                    if summ==targetSum:
                        return True
                if curr.left:
                    q.append((curr.left,summ+curr.left.val))
                if curr.right:
                    q.append((curr.right,summ+curr.right.val))

        return False

