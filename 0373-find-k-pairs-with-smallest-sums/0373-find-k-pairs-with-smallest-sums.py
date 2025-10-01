class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = [(nums1[0]+nums2[0],(0,0))]
        res = []
        print(pq)
        visit = set()
        while pq and len(res)<k:
            summ,cord = heapq.heappop(pq)
            x,y = cord[0],cord[1]
            res.append([nums1[x],nums2[y]])
            if y+1 < len(nums2) and (x,y+1) not in visit:
                visit.add((x,y+1))
                heapq.heappush(pq,(nums1[x]+nums2[y+1],(x,y+1)))
            if x+1 < len(nums1) and (x+1,y) not in visit:
                visit.add((x+1,y))
                heapq.heappush(pq,(nums1[x+1]+nums2[y],(x+1,y)))
        return res
