class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while j>=i:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid

            if nums[mid] >= nums[i]:
                # left side is valid
                if target >= nums[i] and target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1

            else:
                if target > nums[mid] and target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1

            
        return -1