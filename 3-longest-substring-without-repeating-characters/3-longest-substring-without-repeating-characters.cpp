class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = INT_MIN;
        int n = s.size();
        if(n==0)return 0;
        if(n==1)return 1;
        map<char,int> mp;
        int r = 0,i=0;
        while(i<n)
        {
            if(r==n)
            {
                break;
            }
            if(mp.find(s[r])!=mp.end())
            {
                if(i > mp[s[r]])
                {
                    mp[s[r]] = r;
                    r++;
                }
                else {
                    len = max(len, r-i);
                    cout<<"len"<<r<<endl;
                    i = mp[s[r]]+1;
                    mp[s[r]] = r;
                    cout<<"new : "<<s[r]<<" : "<<r<<endl;
                    r++;
                }
            }
            else
            {
                mp[s[r]] = r;
                r++;
            }
        }
        len = max(len, r-i);
        return len;
    }
};