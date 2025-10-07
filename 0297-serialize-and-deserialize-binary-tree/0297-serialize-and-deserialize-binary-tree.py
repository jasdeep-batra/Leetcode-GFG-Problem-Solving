# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #level order traversal
        if not root:
            return ""
        q = [root]
        ans = ""
        while q:
            for i in range(len(q)):
                curr = q.pop(0)
                if curr==None:
                    ans+=str("None")+','
                    continue
                ans+=str(curr.val)+','
                q.append(curr.left)
                q.append(curr.right)
        
        print(ans)
        return ans

    

    def deserialize(self, data):
        if not data:
            return None
        
        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        q = deque([root])
        i = 1  # pointer to track next node value
        
        while q:
            node = q.popleft()
            
            # left child
            if i < len(arr) and arr[i] != "None":
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1
            
            # right child
            if i < len(arr) and arr[i] != "None":
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1
        
        return root




        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))