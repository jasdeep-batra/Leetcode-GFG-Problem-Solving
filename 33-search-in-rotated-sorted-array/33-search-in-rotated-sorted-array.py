class Solution:
    def bs(self,nums, first, last,target):
        while last>=first:
            mid = first +(last-first)//2
            if target==nums[mid]:
                return mid
            if target > nums[mid]:
                first = mid+1;
            else:
                last = mid-1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        n = len(nums)
        if n==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        
        index = -1
        while last>=first:
            mid = first + (last-first)//2
            midl = (n + mid-1)%n
            midr = (mid+1)%n
            if nums[mid] < nums[midl] and nums[mid] < nums[midr]:
                index = mid
                break
            elif nums[mid] < nums[first]:
                last = mid-1
            elif nums[mid] > nums[last]:
                first = mid+1
            else:
                index = first
                break
        print("index: ", index)
        obj = Solution()
        f1 = obj.bs(nums,0,index-1,target)
        f2 = obj.bs(nums,index,n-1,target)
        if(f1==-1 and f2==-1):
            return -1
        if(f1==-1):
            f1 = f2
        return f1
                
        