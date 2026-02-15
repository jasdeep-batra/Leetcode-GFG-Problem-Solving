class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i,j = max(weights),sum(weights)
        def canShip(maxWeight):
            #determine days it will take with this much weight to ship all the container
            summ = 0
            day = 1
            for i in range(len(weights)):
                summ+=weights[i]
                if summ > maxWeight:
                    day+=1
                    summ = weights[i]
            # print(day)
            return day
        ans = j
        while j>i:            
            mid = (j+i)//2 #current max cap of ship
            if canShip(mid) <=days:
                ans = min(ans,mid)
                j = mid
            else:
                i = mid+1

        return ans