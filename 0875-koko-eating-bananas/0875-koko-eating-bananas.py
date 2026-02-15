class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(sp):
            time_taken = 0
            for ban in piles:
                time_taken+=math.ceil(ban/sp)

            # print(time_taken)

            return math.ceil(time_taken)

        
        i,j = 1,max(piles)
        ans = max(piles)
        while j>i:
            mid = (j+i)//2
            time_taken = helper(mid)
            if time_taken <= h:
                print("time_taken; ",time_taken)
                print(mid)
                ans=min(ans,math.ceil(mid))
                j = mid

            else:
                i = mid+1
        return ans

