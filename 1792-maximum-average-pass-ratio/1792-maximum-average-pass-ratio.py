class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def get_inc(p,q):
            return ((p+1)/(q+1)) - (p/q)
        pass_ratio = [(-get_inc(classes[i][0],classes[i][1]),classes[i][0],classes[i][1]) for i in range(len(classes))]
        heapq.heapify(pass_ratio)

        while extraStudents:
            _,p,q = heapq.heappop(pass_ratio)
            p+=1
            q+=1
            heapq.heappush(pass_ratio,(-get_inc(p,q),p,q))
            extraStudents-=1
        ans = 0
        while pass_ratio:
            _,p,q = heapq.heappop(pass_ratio)
            ans+=(p/q)
        return ans/len(classes)
