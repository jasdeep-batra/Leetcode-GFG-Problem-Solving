class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import defaultdict

        # Count the frequency of each character
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1

        stack = []
        res = []

        for ch in s:
            stack.append(ch)
            freq[ch] -= 1

            # Pop from the stack while the top is the smallest remaining character
            while stack and stack[-1] <= min((c for c in freq if freq[c] > 0), default=stack[-1]):
                res.append(stack.pop())

        # Append any remaining characters in the stack
        res += stack[::-1]
        return ''.join(res)