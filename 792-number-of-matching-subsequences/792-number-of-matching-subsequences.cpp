class Solution {
public:
    bool check(string& s, string& p, int i, int j)
    {
        if(j<=0)return true;
        if(i<=0)return false;
        if(s[i-1]==p[j-1])
        {
            return check(s,p,i-1,j-1);
        }
        return check(s,p,i-1,j);
    }
    int numMatchingSubseq(string s, vector<string>& words) {
        int ans = 0;
        unordered_map<string,bool>mp;
        for(int i=0;i<words.size();i++)
        {
            if(mp.find(words[i])!=mp.end())
            {
                if(mp[words[i]]==true)ans++;
                continue;
            }
            else{
                mp[words[i]] = check(s,words[i],s.size(),words[i].size());
                if(mp[words[i]]==true)ans++;
                    
            }
        }
        return ans;
    }
};