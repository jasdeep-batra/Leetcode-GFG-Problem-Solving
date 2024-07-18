# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    count = 0
    def getLeaf(self, root, distance, cnt):
        if root==None:
            return [0]
        if (not root.left) and (not root.right):
            return [1]
        
        left =self.getLeaf(root.left,distance, cnt)
        right = self.getLeaf(root.right,distance,cnt)

        for i in left:
            for j in right:
                if (i> 0) and (j > 0):
                    if (i+j)<=distance:
                        self.count+=1

        ans = []
        for i in left:
            if i>0 and i<distance:
                ans.append(i+1)
        for i in right:
            if i>0 and i<distance:
                ans.append(i+1)
        return ans



    def countPairs(self, root: TreeNode, distance: int) -> int:
        leafs = []
        cnt = 0
        self.getLeaf(root,distance,cnt)
        return self.count
        








         
        return 2
        