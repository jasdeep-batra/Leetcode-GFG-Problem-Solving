class Solution:
    def uncommonFromSentences(self, s11: str, s22: str) -> List[str]:
        s1 = s11.split(" ")
        s2 = s22.split(" ")
        ans = [item for item in s1 if item not in s2 and s1.count(item)==1]
        ans2 = [item for item in s2 if item not in s1 and s2.count(item)==1]
        return ans+ans2

        