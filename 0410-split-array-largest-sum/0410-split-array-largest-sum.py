class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        i,j = max(nums),sum(nums)
        ans = j
        def get_partition(smm):
            part = 1
            s = 0
            for i in range(len(nums)):
                s+=nums[i]
                if s>smm:
                    part+=1
                    s = nums[i]
            return part

        while j>i:
            mid = (j+i)//2
            part = get_partition(mid)
            if part<=k:
                ans = min(ans,mid)
                j = mid
            else:
                i = mid+1
        return ans
