class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #could be dynamic programming problem
        #in other words divide it n/2 partition sum of them is equal 
        n = len(skill)
        net = sum(skill)
        if (net*2) % n!=0:
            return -1
        sum_req = (net*2)//n #sum of each team required
        
        sort_skill = sorted(skill)
        i,j=0,n-1
        ans = 0
        while(j>i):
            if sort_skill[i]+sort_skill[j]==sum_req:
                ans+=(sort_skill[i]*sort_skill[j])
            else:
                return -1
            j-=1
            i+=1
        # print(teams)
        return ans


        