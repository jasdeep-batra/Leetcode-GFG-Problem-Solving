class Solution:
    def longestDupSubstring(self, s: str) -> str:
        #can we use binary search to have a lenght and then chckif any exist
        left = 1
        right = len(s)
        ans = ""

        def isdup(length):
            mapp  = {}
            i = 0
            for j in range(0,len(s)-length+1):
                ss = s[j:j+length]
                if ss in mapp:
                    return (True,ss)
                mapp[ss] = 1
                i = j
            # print(mapp.ke?ys())
            return (False,"")
                
        while right>=left:
            mid = (left+right)//2
            gett = isdup(mid)
            if gett[0]:
                ans = gett[1]
                left = mid+1
            else:
                right = mid-1
        return ans

