class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        i,j = 1,max(candies)
        def canAllocate(candy):
            count = 0
            can = 0
            for pile in candies:
                count+=(pile//candy)

            return count >= k

        
        while j>i:
            mid = (j+i+1)//2
            if canAllocate(mid):
                i = mid

            else:
                j = mid-1


        return i