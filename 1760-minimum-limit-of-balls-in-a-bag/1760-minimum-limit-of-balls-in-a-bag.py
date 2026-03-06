class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        i,j = 1, max(nums)
        # how many operations for 'mid' max balls in bag
        def canFill(size):
            ans = 0
            for num in nums:
                ans+=((num-1)//size)
            # print(ans)
            return ans <= maxOperations
        ans = 0
        while j>i:
            mid = (j+i)//2
            if canFill(mid):
                j = mid
            else:
                i = mid+1

        return i