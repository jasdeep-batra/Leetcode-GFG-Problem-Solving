class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #mountains
        #maintian a monton incre stack
        #if small value then true
        stack = deque()
        K = -sys.maxsize+1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < K:
                return True
            while stack and nums[i] > stack[-1]:
                K = stack.pop()
            stack.append(nums[i])
            
        return False



            
