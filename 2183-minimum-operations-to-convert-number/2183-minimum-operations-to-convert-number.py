class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        #brute force
        # I think we have multiple possibilities
        #start-> goal , gpal->start
        queue = [start]
        visit = [0]*1001
        visit[start]=1
        n = len(nums)
        ops = 0
        while(len(queue)):
            size = len(queue)    
            while(size>0):
                curr  = queue.pop(0)
                if curr==goal:
                    return  ops
                for i in range(n):
                    a = curr + nums[i]
                    b = curr - nums[i]
                    c =( curr ^ nums[i])
                    if a==goal or b==goal or c==goal:
                        return ops+1
                    if (a>=0 and a<=1000) and visit[a]==0:
                        queue.append(a)
                        visit[a]=1
                    if (b>=0 and b<=1000) and visit[b]==0:
                        queue.append(b)
                        visit[b]=1
                    if (c>=0 and c<=1000) and visit[c]==0:
                        queue.append(c)
                        visit[c]=1
                size-=1
            ops+=1
        return -1
        



        

        
        