# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #we can do it bfs 
        queue = []
        queue.append((root,1))
        ans = float('inf')
        while queue:
            for i in range(len(queue)):
                curr,lev = queue.pop(0)
                if not curr.right and not curr.left:
                    ans = min(ans,lev)
                if curr.right:
                    queue.append((curr.right,lev+1))
                if curr.left:
                    queue.append((curr.left,lev+1))

        return ans

        