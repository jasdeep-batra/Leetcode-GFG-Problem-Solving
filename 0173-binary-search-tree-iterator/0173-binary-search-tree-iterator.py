# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.ptr = None
        self.root  = root
    def next(self) -> int:

        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        
        self.node = self.stack.pop()
        self.root = self.node.right
        return self.node.val



        

    def hasNext(self) -> bool:
        return bool(self.stack) or self.root is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()