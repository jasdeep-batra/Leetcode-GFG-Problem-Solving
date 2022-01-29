class Solution {
public:
    string minWindow(string s, string t) {
        int i=0,j=0;
        map<char,int> mp;
        string res;
        int size = s.size();
        
        for(int i=0;i<t.size();i++)
        {
            mp[t[i]]++;
        }
        int count = mp.size();
        while(j<=s.size())
        {
            if(count>0)
            {
                if(mp.find(s[j])!=mp.end())
                {
                    mp[s[j]]--;
                    if(mp[s[j]]==0)
                    {
                        count--;
                    }
                }
                j++;
            }
            else if(count==0)
            { 
                if((j-i) <= size)
                {
                    string answer = s.substr(i,j-i);
                    res = answer;
                    size = answer.size();
                }
                if(mp.find(s[i])!=mp.end())
                {
                    mp[s[i]]++;
                    if(mp[s[i]]==1)count++;
                }
                i++;                            }
        }
        return res;
    }
};