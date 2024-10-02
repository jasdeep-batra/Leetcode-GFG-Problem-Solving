class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0]*26
        for i in range(len(s)):
            char = ord(s[i]) - ord('a')
            freq[char]+=1
        
        for item in s:
            char = ord(item) - ord('a')
            if freq[char]==1:
                return s.index(item)
        return -1


