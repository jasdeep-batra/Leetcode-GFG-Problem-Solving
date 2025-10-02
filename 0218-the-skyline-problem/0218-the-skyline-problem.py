class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        sorted_build = sorted([(L,-H,R) for L,R,H in buildings] + [(R,0,"any") for L,R,H in buildings])
        # sorted_build.sort()
        pq = [(0,float('inf'))] #max_heap
        res = [[0,0]]
        for x,h,y in sorted_build:
            while x >= pq[0][1]:
                heapq.heappop(pq)

            if -h:
                heapq.heappush(pq,(h,y))
            max_height = -pq[0][0]
            if res[-1][1]!=max_height:
                res.append([x,max_height])

        return res[1:]