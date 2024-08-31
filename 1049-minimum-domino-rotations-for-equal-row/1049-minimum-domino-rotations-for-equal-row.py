class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        mapp = {}
        for i in tops:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i] = 1
        for i in bottoms:
            if i in mapp:
                mapp[i]+=1
            else:
                mapp[i] = 1

        n = len(tops)
        curr_key = 0
        for key,value in mapp.items():
            if value>=n:
                flag = True
                curr_key = key
                break
        cmp1,cmp2,ans1,ans2 = 0,0,0,0
        for i in zip(tops, bottoms):
            if i[0]==curr_key:
                cmp1+=1
            elif i[0]!=curr_key:
                if i[1]==curr_key:
                    cmp1+=1
                    ans1+=1
            if i[1]==curr_key:
                cmp2+=1
            if i[1]!=curr_key:
                if i[0]==curr_key:
                    cmp2+=1
                    ans2+=1


        print(cmp1," ",cmp2)
        if cmp1==n and cmp2==n:
            return min(ans1,ans2) 
        if cmp1==n:
            return ans1
        if cmp2==n:
            return ans2
              
        return -1

        

            
        