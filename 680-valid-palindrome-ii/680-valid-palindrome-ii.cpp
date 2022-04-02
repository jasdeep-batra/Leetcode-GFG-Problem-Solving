class Solution {
public:
    bool validPalindrome(string s) {
        int i=0,j=s.size()-1,flag=0;
        while(i<j)
        {
            if(s[i]!=s[j])
            {
                int ni = i+1,nj = j;
                while(ni<nj && s[ni]==s[nj])
                {
                    ni++;nj--;
                }
                int oi = i,oj = j-1;
                while(oi<oj && s[oi]==s[oj])
                {
                    oi++;oj--;
                }
                return ni>=nj || oi>=oj;
            }
             i++;j--;   
        }
        return true;
    }
};