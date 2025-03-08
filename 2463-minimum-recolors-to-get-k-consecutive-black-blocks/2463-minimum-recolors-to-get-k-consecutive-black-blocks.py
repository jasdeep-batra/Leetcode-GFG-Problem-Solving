class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j = 0, 0
        white = 0  # Corrected initialization

        # First window of size k
        for j in range(k):  # Fixes infinite loop issue
            if blocks[j] == 'W':
                white += 1

        ans = white  # Store the initial white count

        # Sliding window technique
        for j in range(k, len(blocks)):  
            if blocks[j] == 'W':
                white += 1
            if blocks[i] == 'W':
                white -= 1
            i += 1  # Move window forward
            ans = min(ans, white)  # Update minimum whites to be recolored

        return ans
