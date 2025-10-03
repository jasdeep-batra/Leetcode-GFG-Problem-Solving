# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #it works like L M R 
        arr = []
        def dfs(r):
            if not r:
                return None
            dfs(r.left)
            arr.append(r.val)
            dfs(r.right)
        dfs(root)
        return arr
    
        
        