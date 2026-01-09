class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalised_string = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                normalised_string += (s[i].lower() if s[i].isalpha() else s[i])

        return normalised_string==normalised_string[::-1]

