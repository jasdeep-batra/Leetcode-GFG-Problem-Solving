class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while right > left:
            mid = (left+right)//2
            if nums[mid]>=0:
                right = mid
            else:
                left = mid+1
        return max(left,len(nums)-left-nums.count(0))

            




