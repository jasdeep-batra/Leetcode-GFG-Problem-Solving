class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for item in words:
            b = len(pref)
            a = item[:b]
            if a==pref:
                ans+=1

        return ans
        