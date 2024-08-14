class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1]-nums[0]
        while high > low:
            mid = (high+low)//2
            if self.helper(nums,mid) < k:
                low = mid+1
            else:
                high = mid
        return low

    def helper(self,nums,mid):
        count = left = 0
        for right in range(1,len(nums)):
            while nums[right]-nums[left] > mid:
                left +=1
            count += right-left
        return count

        