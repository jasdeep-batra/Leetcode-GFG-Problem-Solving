class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [(nums1[0]+nums2[0],0,0)]
        res = []
        visit = set()
        while pq:
            s,x,y = heapq.heappop(pq)
            res.append([nums1[x],nums2[y]])
            if len(res)==k:
                break
            if x+1<len(nums1) and (x+1,y) not in visit:
                heapq.heappush(pq,(nums1[x+1]+nums2[y],x+1,y))
                visit.add((x+1,y))
            if y+1<len(nums2) and (x,y+1) not in visit:
                heapq.heappush(pq,(nums1[x]+nums2[y+1],x,y+1))
                visit.add((x,y+1))

        return res

        


