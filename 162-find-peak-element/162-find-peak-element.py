class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        f = 0
        l = len(nums)-1
        n = len(nums)
        if n==1:
            return 0
        while l >= f:
            mid = f + (l-f)//2
            if((mid > 0) and (mid < n-1)):
                if ((nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1])):
                    return mid
                elif nums[mid-1] > nums[mid+1]:
                    l = mid-1
                elif nums[mid+1] >= nums[mid-1]:
                    f = mid+1
            elif(mid==0):
                if(nums[mid]>nums[mid+1]):
                    return mid
                else:
                    return mid+1
            elif(mid==n-1):
                if(nums[mid] > nums[mid-1]):
                    return mid
                else:
                    return mid-1
        return -1
        
        