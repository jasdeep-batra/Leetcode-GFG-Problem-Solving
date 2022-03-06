class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        //npm
        int length = s.size();
        int i=0,j=1;
        vector<int> lps(s.size(),0);
       // map<int,int> mp;
        while(j<s.size())
        {
            if(s[i]==s[j])
            {
                lps[j] = i+1;
                i++;j++;               
            }
            else if(i==0)
            {
                j++;
            }
            else
            {
                i = lps[i-1];
            }
        }
        return lps.back() && s.size()%(s.size()-lps[lps.size()-1])==0;
    }
};