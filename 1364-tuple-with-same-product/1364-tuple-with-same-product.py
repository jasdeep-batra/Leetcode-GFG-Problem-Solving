class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        #mathematical question
        #there must be certain condition we have to find; 
        #it could be a problem of suffix and prefix
        #sorting could be helpful
        #for one tuple there will be 8 solutions
        # 10^12  -> x o(n2)
        #binary search
        num = sorted(nums)
        dictt = {}
        ans = 0
        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                prod = num[i]*num[j]
                if prod in dictt:
                    ans+=dictt[prod]
                    dictt[prod]+=1
                else:
                    dictt[prod] = 1
            print(ans)
        return ans*8

                    







        