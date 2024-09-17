class Solution:
    def uncommonFromSentences(self, s11: str, s22: str) -> List[str]:
        s1 = s11.split(" ")
        s2 = s22.split(" ")
        return [item for item in s1 if item not in s2 and s1.count(item)==1]+[item for item in s2 if item not in s1 and s2.count(item)==1]

        