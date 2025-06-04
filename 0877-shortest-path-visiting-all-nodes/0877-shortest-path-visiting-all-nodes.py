class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        #adj is already provided
        #if we have limited nodes we can create its state
        # 1->12 binary number do determine if all node were visited
        #do wee need to see indegree and outdegree
        #start with the min indegree elements
        #those who have single or lowest degree will be source then point no 3
        #either start from every node but with dp array we can check if value less
        #how revisit is handles because we are checking combination of state, node not just node so even if revisit the state will be different
        visit = set()
        n = len(graph)
        target = (1 << n) - 1
        queue = deque()
        visit = set()
        for i in range(n):
            queue.append((i,1<<i))
            visit.add((i,1<<i))

        step = 0
        while queue:
            for _ in range(len(queue)):
                node,state = queue.popleft()
                if state==target:
                    return step
                
                for child in graph[node]:
                    new_mask = state | 1<<child
                    if (child,new_mask) not in visit:
                        visit.add((child,new_mask))
                        queue.append((child,new_mask))

            step+=1
        return -1
