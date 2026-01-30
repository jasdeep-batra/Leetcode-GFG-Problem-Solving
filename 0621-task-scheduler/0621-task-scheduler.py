class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = Counter(tasks)
        pq = []
  #      task = 0
        for key,value in freq_dict.items():
            heapq.heappush(pq,-value)
        top = -heapq.heappop(pq)
        task = top + (top-1)*n
        while pq:
            if -pq[0] == top:
                task+=1
            heapq.heappop(pq)
        if task < len(tasks):
            return len(tasks)
        return task