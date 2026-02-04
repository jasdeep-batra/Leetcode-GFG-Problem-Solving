# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.store = {0:1}
        self.ans = 0
        def dfs(node,summ):
            if not node:
                return 
            summ+=node.val            
            self.ans+=self.store.get(summ-targetSum,0)
            # print("heyy")
            self.store[summ] = self.store.get(summ,0)+1
            dfs(node.left,summ)
            dfs(node.right,summ)
            self.store[summ]-=1

            return
        dfs(root,0)
        print(self.store)
        return self.ans