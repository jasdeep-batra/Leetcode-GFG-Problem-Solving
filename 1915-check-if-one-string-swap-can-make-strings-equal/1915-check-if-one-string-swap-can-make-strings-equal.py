class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True  # Already equal

        # Find the indices where s1 and s2 differ
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]

        # There must be exactly two differences, and swapping them should fix the issue
        return len(diff) == 2 and diff[0] == diff[1][::-1]
