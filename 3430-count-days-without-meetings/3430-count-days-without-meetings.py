class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        #constraint are too high
        #we have to find no of days
        #can we merge them and if there is any gap we will add to the answer
        ans = 0
        meetings.sort()
        if meetings[0][0] > 1:
            ans+=meetings[0][0]-1
        last = meetings[0][1]
        print(meetings)
        for i in range(1,len(meetings)):
            cstart,cend = meetings[i][0],meetings[i][1]
            if cstart > last:
                ans+=(cstart-last-1)
            last = max(cend,last)

        return ans+days-last
                
        
            


        