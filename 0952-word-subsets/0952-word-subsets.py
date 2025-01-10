from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # All words in words2 should be subsets of words in words1.

        def freqWord2(words2):
            arr = [0] * 26
            for word in words2:
                freq = [0] * 26  # Added initialization of `freq` inside the loop
                for w in word:
                    freq[ord(w) - ord('a')] += 1
                for i in range(26):
                    arr[i] = max(arr[i], freq[i])  # Fixed `freq(i)` to `freq[i]`
            return arr

        res = []
        arr = freqWord2(words2)  # No changes here
        for word in words1:
            flag = False
            freq = [0] * 26
            for w in word:
                freq[ord(w) - ord('a')] += 1
            for i in range(26):
                if freq[i] < arr[i]:
                    flag = True
                    break  # Added `break` to exit early if condition is met
            if not flag:
                res.append(word)

        return res
