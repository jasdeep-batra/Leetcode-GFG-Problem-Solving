class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero,one,two = 0,0,0
        for item in nums:
            if item==0:
                zero+=1
            if item==1:
                one+=1
            if item==2:
                two+=1

        for i in range(len(nums)):
            if zero:
                nums[i] = 0
                zero-=1
            elif one:
                nums[i] = 1
                one-=1
            elif two:
                nums[i] = 2
                two-=1
        """
        Do not return anything, modify nums in-place instead.
        """
        