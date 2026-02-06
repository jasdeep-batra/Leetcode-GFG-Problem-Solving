class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        j = 0
        while j < k:
            while stack and stack[-1] < nums[j]:
                stack.pop()
            stack.append(nums[j])

            j+=1


        res = [stack[0]]
        while j < len(nums):
            if nums[j-k] == stack[0]:
                stack.popleft()

            while stack and nums[j] > stack[-1]:
                stack.pop()
            
            stack.append(nums[j])

            res.append(stack[0])
            j+=1
        return res