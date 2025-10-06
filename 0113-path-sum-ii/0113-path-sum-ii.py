# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # can we store a array in a queue or a string
        if not root:
            return []
        #either dfs or bfs
        q = [(root,root.val,[root.val])]
        res = []
        while q:
            for i in range(len(q)):
                curr,summ,arr = q.pop(0)
                if not curr.left and not curr.right:
                    if summ==targetSum:
                        res.append(arr)
                if curr.left:
                    q.append((curr.left,summ+curr.left.val,arr+[curr.left.val]))
                if curr.right:
                    q.append((curr.right,summ+curr.right.val,arr+[curr.right.val]))
        # print(res)
        return res