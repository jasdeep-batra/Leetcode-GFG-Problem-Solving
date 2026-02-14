class Solution:
    def findMin(self, nums: List[int]) -> int:
        if  nums[0] < nums[-1]:
            return nums[0]
        n = len(nums)
        i,j = 0,n-1
        while j>i:
            mid = (j+i)//2
            if (nums[mid] > nums[j]):
                i = mid+1
            else:
                j = mid
            
        return nums[i]