class Solution:
    def checkValidString(self, s: str) -> bool:
        o = 0
        c = 0
        for item in s:
            if item=='(' or item=='*':
                o+=1
            if item==')':
                c+=1
            if c > o:
                return False
        o,c = 0,0
        for item in reversed(s):
            if item==')' or item=='*':
                c+=1
            else:
                o+=1
            if o > c:
                return False
        return True
        