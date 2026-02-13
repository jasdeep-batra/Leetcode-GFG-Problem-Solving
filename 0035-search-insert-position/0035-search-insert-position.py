class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        ind = 0

        while j>=i:
            mid = (j+i)//2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                i = mid+1
            else:
                j =mid-1

        return i
