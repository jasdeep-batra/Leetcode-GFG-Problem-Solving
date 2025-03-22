class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = [0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indeg[u]+=1
        

        q = deque([])
        for i in range(len(indeg)):
            if indeg[i]==0:
                q.append(i)
        ans = 0
        while q:
            curr = q.pop()
            ans+=1
            for neg in graph[curr]:
                indeg[neg]-=1
                if indeg[neg]==0:
                    q.append(neg)

        return ans==numCourses

        
                    







        