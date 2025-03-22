class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        indeg = [0]*numCourses
        graph = defaultdict(list)
        for u,v in pre:
            graph[v].append(u)
            indeg[u]+=1
        # if not pre:
            # return [i for i in range(numCourses-1,-1,-1)]
        ans = []
        q = deque([index for index,item in enumerate(indeg) if item==0])
        while q:
            print("in")
            curr = q.pop()
            print(curr)
            ans.append(curr)
            for nbr in graph[curr]:
                indeg[nbr]-=1
                if indeg[nbr]==0:
                    q.append(nbr)
        print(ans)
        return ans if len(ans)==numCourses else []