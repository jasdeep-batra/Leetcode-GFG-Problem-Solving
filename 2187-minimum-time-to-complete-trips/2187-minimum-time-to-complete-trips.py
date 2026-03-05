class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i,j = 1,max(time)*totalTrips
        def canTravel(tim):
            total = 0
            for t in time:
                total += (tim//t)

            return total >= totalTrips

        while j>i:
            mid = (j+i)//2
            if canTravel(mid):
                j = mid

            else:
                i = mid+1
        return i


