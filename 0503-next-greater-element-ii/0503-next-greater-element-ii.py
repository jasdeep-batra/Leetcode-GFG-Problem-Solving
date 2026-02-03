class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            
            while stack and nums[i] > nums[stack[-1]%n]:
                ind = stack.pop()
                res[ind%n] = nums[i]

            stack.append(i)

        return res[:n]