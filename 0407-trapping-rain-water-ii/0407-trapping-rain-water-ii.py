class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        #do we need to find the block whose boundry has greater height.
        #assume it as 2d map and we need to find the blocks with less number than boundry
        # or we can slice
        #pq will be use to start from smallest height blocks 
        pq =  []
        visit = [[False]*len(heightMap[0]) for _ in range(len(heightMap))]
        for i,row in enumerate(heightMap):
            for j in range(len(row)):
                if i==0 or i==len(heightMap)-1 or j==0 or j==len(row)-1:
                    heapq.heappush(pq,(row[j],i,j))
                    visit[i][j] = True

        #go fo the bfs
        res = 0
        while pq:
            h,i,j = heapq.heappop(pq)
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                x,y = i+dx,j+dy
                if x>=0 and x<len(heightMap) and y>=0 and y<len(heightMap[0]) and not visit[x][y]:
                    visit[x][y]=True
                    nh = heightMap[x][y]
                    if h>nh:
                        res+=(h-nh)

                    heapq.heappush(pq,(max(nh,h),x,y))

        return res
