class Solution {
public:
    int strStr(string haystack, string needle) {
        //LPS : longest prefix same as suffix;
        if(needle.empty())return 0;
        vector<int> lps(needle.size(),0);
        int i=0,j=1;
        while(j<needle.size())
        {
            if(needle[i]==needle[j])
            {
                lps[j] = i+1;i++;j++;
            }
            else
            {
                if(i!=0)
                {
                    i = lps[i-1];                    
                }
                else
                {
                    lps[j] = 0;
                    j++;
                }                                
            }
        }
        for(auto itr: lps)
        {
            cout<<itr<<endl;
        }
        int m = 0;
        int n = 0;
        while(m<haystack.size())
        {
            if(haystack[m]==needle[n])
            {
                m++;
                n++;
            }
            if(n==needle.size())
            {
                int ans = m-n;
                return ans;
            }
            if(haystack[m]!=needle[n])
            {
                if(n!=0)
                {
                    n = lps[n-1];                    
                }
                else
                {
                    m++;                    
                }
            }            
        }
        return -1;
    }
};