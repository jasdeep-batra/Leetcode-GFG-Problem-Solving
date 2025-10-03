# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        toggle = 0
        while q:
            length = len(q)
            # print(length)
            ans = []
            for i in range(length):
                curr = q.pop(0)
                # print(curr.val)
                ans.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if toggle%2==1:
                ans.reverse()
            res.append(ans) 
            toggle+=1
                    

        return res



        