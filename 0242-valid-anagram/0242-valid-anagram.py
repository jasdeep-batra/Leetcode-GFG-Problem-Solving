class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char = [0 for i in range(26)]
        for c in s:
            char[ord(c)-ord('a')]+=1
        for c in t:
            char[ord(c)-ord('a')]-=1
        
        for i in char:
            if i!=0:
                return False
        return True