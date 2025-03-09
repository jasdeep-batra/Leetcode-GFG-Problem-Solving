from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors += colors  # Handle circular behavior
        i, j = 0, 1  # Start and end of the sliding window
        count = 0

        while i < n:
            if j - i < k:  # Expand window up to size k
                if colors[j] != colors[j - 1]:  # Check alternating pattern
                    j += 1
                else:
                    i = j  # Reset start position
                    j += 1
            else:  # If window reaches size k
                count += 1  # Valid alternating window found
                i += 1  # Slide window forward
                if colors[i] == colors[i - 1]:  # If not alternating anymore, reset window
                    j = i + 1

        return count
