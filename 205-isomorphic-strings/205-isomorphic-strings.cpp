class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char,char> mp,tmp;
        if(s.size()!=t.size())return false;
        for(int i=0;i<s.size();i++)
        {
            if(mp.find(s[i])!=mp.end()){
                if(t[i]!=mp[s[i]])return false;
            }
            if(tmp.find(t[i])!=tmp.end())
            {
                if(tmp[t[i]]!=s[i])return false;
            }
            mp[s[i]] = t[i];
            tmp[t[i]] = s[i];
        }
        return true;
    }
};