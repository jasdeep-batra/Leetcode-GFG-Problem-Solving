class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sC= Counter(s)
        tC= Counter(t)
        tmp = sC & tC
        tmpSum = sum(tmp.values())
        return len(s) + len(t) - tmpSum - tmpSum