# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        self.res = []
        def preorder(node):
            if not node:
                return
            self.res.append(node.val)
            preorder(node.left)
            preorder(node.right)

            return
        preorder(root)
        ans = ""
        for val in self.res:
            ans+=str(val)+'+'
        print("ans ",ans)
        return ans
            
            
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        ndta = data.split('+')
        print(ndta)
        arr = [int(ndta[i]) for i in range(len(ndta)-1)]
        print("arr", arr)
        self.i = 0
        def createTree(i,ub):
            if self.i==len(arr) or arr[self.i]  > ub:
                return None
            node = TreeNode(arr[self.i]) 
            self.i+=1
            node.left = createTree(self.i,node.val)
            node.right = createTree(self.i,ub)
            return node
        return createTree(0,sys.maxsize)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans