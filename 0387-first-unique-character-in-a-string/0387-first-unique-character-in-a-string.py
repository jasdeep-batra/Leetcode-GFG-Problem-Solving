class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = [0]*26  # O(1)
        for item in s:
            char[ord(item)-ord('a')]+=1
    
        for i in range(len(s)):
            if char[ord(s[i])-ord('a')]==1:
                return i
        return -1
