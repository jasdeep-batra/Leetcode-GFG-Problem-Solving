class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        arr = sorted(courses,key = lambda x:x[1])
        print(arr)

        total_dur = 0
        pq = []
        ans = 0
        for d,l in arr:
            total_dur+=d            
            heapq.heappush(pq,-d)
            if total_dur > l:
                total_dur+=heapq.heappop(pq)

        return len(pq)