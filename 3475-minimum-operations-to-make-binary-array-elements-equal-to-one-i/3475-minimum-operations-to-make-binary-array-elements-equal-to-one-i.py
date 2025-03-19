class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-3):
            if nums[i]==0:
                nums[i] = 1
                nums[i+1]^=1
                nums[i+2]^=1
                count+=1
        print(nums)
        zero = nums.count(0)
        if zero%3!=0:
            return -1
        return count+1 if zero!=0 else count

            