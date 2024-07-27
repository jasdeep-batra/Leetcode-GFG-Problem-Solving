class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for  i in s:
            if i.isalpha() or i.isnumeric():
                news+=i
        
        
        newss = news[::-1]

    
        return newss.lower()==news.lower()
        