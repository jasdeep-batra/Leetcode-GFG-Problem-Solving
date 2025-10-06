# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-float('inf')]
        def dfs(node):
            if not node:
                return 0
            
            left_sum = max(dfs(node.left),0)
            right_sum = max(dfs(node.right),0)
            # print(left_sum+node.val+right_sum)
            ans[0] = max(ans[0],left_sum+node.val+right_sum,node.val)

            return node.val+max(left_sum,right_sum)
        sol = dfs(root)
        return ans[0]
        