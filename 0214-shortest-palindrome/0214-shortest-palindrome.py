class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 0
        power = 1
        last = 0
        for i,c in enumerate(s):
            char = ord(c) - ord('a')+1

            #prefix = new number will be a new unit place 
            prefix = prefix*29
            prefix += char

            #suffix = new number will be then 29^i th place and first number is  a unit here.
            suffix  = suffix + char*power
            power = power*29

            if prefix==suffix:
                last = i

        rem = s[last+1:]
        return rem[::-1]+ s
        