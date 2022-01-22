class Solution:
    def firste(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums)-1
        res = -1;
        while f <= l:
            mid = f + (l-f)//2
            if(nums[mid]==target):
                res = mid
                l = mid-1
            elif nums[mid] > target:
                l = mid-1
            else:
                f = mid+1
        return res
    
    def laste(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums)-1
        res = -1;
        while f <= l:
            mid = f +((l-f)//2)
            if(nums[mid]==target):
                res = mid
                f = mid+1
            elif nums[mid] > target:
                l = mid-1
            else:
                f = mid+1
        return res
                
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if len(nums)==0:
        #     return [-1,-1]
        obj = Solution()
        f = obj.firste(nums,target)
        l = obj.laste(nums,target)
        result = [f,l]
        return result
        
        