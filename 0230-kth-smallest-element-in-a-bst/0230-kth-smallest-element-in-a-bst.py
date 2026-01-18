# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        max_heap = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if len(max_heap) < k:
                    heapq.heappush(max_heap,-curr.val)
                else:
                    if curr.val < -max_heap[0]:
                        heapq.heappop(max_heap)
                        heapq.heappush(max_heap,-curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return -max_heap[0]

            