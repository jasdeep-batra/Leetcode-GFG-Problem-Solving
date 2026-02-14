class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i,j = 0,len(nums)-1
        while j>=i:
            mid = (i+j)//2
            if nums[mid]==target:
                return True


            if nums[mid]==nums[i]==nums[j]:
                i+=1
                j-=1

            elif nums[mid] >= nums[i]:
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

            
        return False