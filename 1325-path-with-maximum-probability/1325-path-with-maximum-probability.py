class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adl = [[] for _ in range(n)]
        j = 0
        for edge in edges:
            u,v = edge[0],edge[1]
            adl[u].append((v,succProb[j]))
            adl[v].append((u,succProb[j]))
            j+=1

        max_prob = [0.0]*n
        max_prob[start_node] = 1.0
        queue = [(-1.0,start_node)]
        while(queue):
            prob,curr = heapq.heappop(queue)
            prob = -prob
            if curr==end_node:
                return prob
            childs = adl[curr]
            for child,cprob in childs:
                curr_prob = prob*cprob
                if curr_prob > max_prob[child]:
                    max_prob[child] = curr_prob
                    heapq.heappush(queue,(-curr_prob,child))

        return 0.0

        