class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length of the string is odd, it's impossible to balance
        if len(s) % 2 != 0:
            return False

        # Check left-to-right balance
        open_count = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':  # '(' or flexible
                open_count += 1
            else:  # ')'
                open_count -= 1
            
            # If there are more ')' than '(', it's invalid
            if open_count < 0:
                return False

        # Check right-to-left balance
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':  # ')' or flexible
                close_count += 1
            else:  # '('
                close_count -= 1
            
            # If there are more '(' than ')', it's invalid
            if close_count < 0:
                return False

        # If both checks pass, the string can be valid
        return True
