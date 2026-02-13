class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,len(nums)-1
        mi,mxi = len(nums),-1
        ind = len(nums)
        while j>=i:
            mid = (j+i)//2
            if nums[mid]==target:
                ind = mid
                break

            if target < nums[mid]:
                j = mid-1
            else:
                i = mid+1

        mi = ind-1
        while mi >=0:
            if nums[mi]!=target:
                break
            mi-=1
        
        mx = ind+1
        while mx<len(nums):
            if nums[mx]!=target:
                break
            mx+=1

        return [mi+1,mx-1] if ind!=len(nums) else [-1,-1]
