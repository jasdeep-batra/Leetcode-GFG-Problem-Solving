# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_dict = defaultdict(int)
        for index,node in enumerate(inorder):
            in_order_dict[node] = index
        
        root = None
        def helper(ps,pe,istart,iend):
            #base condition
            if pe<ps or iend<istart:
                return None
            root=TreeNode(preorder[ps])
            index = in_order_dict[preorder[ps]]
            l,r = index-istart, iend-index
            root.left = helper(ps+1,ps+l+1,istart,index-1)
            root.right = helper(ps+l+1,ps+l+r,index+1,iend)
            return root

        return helper(0,len(preorder)-1,0,len(inorder)-1)