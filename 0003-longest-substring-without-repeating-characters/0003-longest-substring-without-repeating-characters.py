class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = {}
        ans = float('-inf')
        i=0
        for j in range(len(s)):
            if s[j] not in mapp:
                mapp[s[j]] = j

            else:
                print(j)
                print(i)
                print("----------")
                ans = max(ans,j-i)
                if mapp[s[j]] >= i:
                    i = mapp[s[j]]+1
                mapp[s[j]] = j
        
        print(mapp)
        if ans==float('-inf'):
            ans = len(s)
        else:
            print(i)
            ans = max(ans,len(s)-i)


        return ans
