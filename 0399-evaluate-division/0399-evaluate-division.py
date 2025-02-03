class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for index,equation in enumerate(equations):
            u,v= equation[0],equation[1]
            if u not in graph:
                graph[u] = {v:values[index]}
            if u in graph:
                graph[u][v] = values[index]
            if v not in graph:
                graph[v] = {u:1/values[index]}
            if v in graph:
                graph[v][u] = 1/values[index]

        print(graph)
        
        def dfs(start,end,visit):
            if start not in graph:
                return -1.0
            if end in graph[start]:
                return graph[start][end]

            visit.add(start)
            for neighbour,value in graph[start].items():
                if neighbour not in visit:
                    productWeight = dfs(neighbour,end,visit)
                    if productWeight!=-1.0:
                        return productWeight * value
            return -1.0

        res = []
        for query in queries:
            start = query[0]
            end = query[1]
            visit = set()
            ans = dfs(start,end,visit)
            res.append(ans)

        return res



        
            
            


        