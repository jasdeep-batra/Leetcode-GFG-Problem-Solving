class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans =1
        count = 1
        prev = word[0]
        for i in range(1,len(word)):
            if word[i]!=prev:
                ans+=count-1
                prev = word[i]
                count = 1
            else:
                count+=1

        ans += count-1
        return ans


        