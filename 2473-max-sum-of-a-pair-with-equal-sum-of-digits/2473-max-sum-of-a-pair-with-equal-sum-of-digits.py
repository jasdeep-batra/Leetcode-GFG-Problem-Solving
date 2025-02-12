class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def add(s):
            ans = 0
            for i in s:
                ans+=int(i)
            return ans
        dictt = {}
        res = 0
        for num in nums:
            snum = str(num)
            sadd = add(snum)
            if  sadd in dictt:
                res = max(res,int(num)+dictt[sadd])
                if int(num) > dictt[sadd]:
                    dictt[sadd] = int(num)
            else:
                dictt[sadd] = int(num)
        return res if res!=0 else -1




        