class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9+7
        #top down approach
        dictt = {}
        def recurison(i,person,prof):
            #base condition (will be tricker to write)
            # I think we have to use for loop if normal doesn't work
            if i>=len(profit) or person<=0:
                return 1 if prof >= minProfit else 0
            if (i,person,prof) in dictt:
                return dictt[(i,person,prof)]
            scheme = 0
            if person >= group[i]:
                scheme +=recurison(i+1,person-group[i],min(minProfit,prof+profit[i]))
            scheme += recurison(i+1,person,prof)
            # print(scheme)
            dictt[(i,person,prof)] = scheme%MOD
            return scheme%MOD
        return recurison(0,n,0)%MOD
