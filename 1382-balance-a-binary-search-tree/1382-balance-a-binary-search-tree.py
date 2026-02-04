# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.inor = []
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.inor.append(node.val)
            inorder(node.right)

        inorder(root)
        def create_tree(left,right):
            if left>right:
                return None
            i,j = left,right
            mid = (j+i)//2
            node = TreeNode(self.inor[mid])
            node.left = create_tree(left,mid-1)
            node.right = create_tree(mid+1,right)

            return node
        
        return create_tree(0,len(self.inor)-1)