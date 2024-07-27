class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def rec(ss, tt, i, j):
            if i >= len(ss):
                return True
            if j >= len(tt):
                return False
            if ss[i] == tt[j]:
                return rec(ss, tt, i + 1, j + 1)
            else:
                return rec(ss, tt, i, j + 1)

        return rec(s, t, 0, 0)
        