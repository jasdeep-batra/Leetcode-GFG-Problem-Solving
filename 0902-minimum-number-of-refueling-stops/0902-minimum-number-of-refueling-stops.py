class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel>=target:
            return 0
        heapq.heapify(stations)
        dist = 0
        current_fuel = startFuel
        prev_dist = 0
        max_heap = []
        count = 0
        while current_fuel<target:
            while stations and current_fuel >= stations[0][0]:
                dist,fuel = heapq.heappop(stations)
                heapq.heappush(max_heap,(-fuel,dist))

            if not max_heap:
                return -1
            
            f,d = heapq.heappop(max_heap)
            current_fuel+=(-f)
            count+=1

        return count


