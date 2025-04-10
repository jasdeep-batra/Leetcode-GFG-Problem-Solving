class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num-1]<0:
                # print(num,":",nums[num-1])
                return num
            nums[num-1] = -nums[num-1]
        # print(nu/ms)
        return 0
        