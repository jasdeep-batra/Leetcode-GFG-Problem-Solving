class Solution {
public:
    bool validPalindrome(string s) {
        //if the entire string is a palindrome then first and last element should match
        // so we'll use two pointer approach and we can only remove one element  if we reaches the point where we are gonna remove multiple char then we will stop
        int i = 0;
        int j = s.size()-1;
        while(j>i)
        {
            if(s[i]!=s[j])            
            {
                int ni = i+1;
                int nj = j;
                while(nj>ni && s[ni]==s[nj])
                {
                    ni++;
                    nj--;
                }
                int oi = i;
                int oj = j-1;
                while(oj>oi && s[oi]==s[oj])
                {
                    oi++;
                    oj--;
                }
                return ni>=nj || oi>=oj;
            }
            i++;
            j--;
        }
        return true;
    }
};