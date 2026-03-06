class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        #we can determine if that distance is kthe one by counting all shorter distance

        nums.sort()
        i,j = 0, nums[-1] - nums[0]
        def isReq(d):
            left= 0
            ans = 0
            for right in range(len(nums)):
                while nums[right]-nums[left] > d:
                    left+=1
                ans += (right-left)

            return ans
                
        while j>i:
            mid = (j+i)//2
            cnt= isReq(mid)
            if cnt>=k:
                j = mid
            
            else:
                i = mid+1
        return i