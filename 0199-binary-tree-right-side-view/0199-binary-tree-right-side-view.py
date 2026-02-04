# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        #related to level order traversal
        #can we store current id on the level 
        level = {}
        queue = deque([(root,0)])
        level[0] = root
        while queue:
            curr,lev = queue.popleft()
            if curr.right:
                if (lev+1) not in level:
                    level[lev+1] = curr.right
                queue.append((curr.right,lev+1))
            if curr.left:
                if (lev+1) not in level:
                    level[lev+1] = curr.left
                queue.append((curr.left,lev+1))
            
        res = []
        for key,v in level.items():
            print(key," : ",v)
        for value in level.values():
            res.append(value.val)
        return res
        
