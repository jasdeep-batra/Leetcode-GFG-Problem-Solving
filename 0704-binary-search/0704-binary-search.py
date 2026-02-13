class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while j>=i:
            mid = (j+i)//2
            if nums[mid]==target:
                return mid

            if nums[mid] > target:
                j = mid-1
            else:
                i = mid+1

        return -1