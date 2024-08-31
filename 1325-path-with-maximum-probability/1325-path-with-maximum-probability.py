class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        max_prob = [0.0]*n
        adl = [[] for _ in range(n)]
        j = 0
        for edge in edges:
            v = edge[0]
            u = edge[1]
            prob = succProb[j]
            adl[v].append((u,prob))
            adl[u].append((v,prob))
            j+=1
        max_prob[start_node] = 1.0
        priority_queue = []
        heapq.heappush(priority_queue,(-1.0,start_node))
        while priority_queue:
            prob,curr = heapq.heappop(priority_queue) #tuple
            prob = -prob
            if curr==end_node:
                return prob
            childs = adl[curr]
            for child,cprob in childs:
                new_prob = prob*cprob
                if new_prob > max_prob[child]:
                    max_prob[child] = new_prob
                    heapq.heappush(priority_queue,(-new_prob,child))
            

        return 0.0





        