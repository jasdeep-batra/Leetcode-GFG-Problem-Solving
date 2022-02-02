class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        // sliding window
        map<char,int> mp;
        for(int i=0;i<p.size();i++)
        {
            mp[p[i]]++;
        }
        int count = mp.size();
        vector<int> result;
        int k = p.size(),i=0,j=0;
        while(j<s.size())
        {
            if(mp.find(s[j])!=mp.end())
            {
                mp[s[j]]--;
                if(mp[s[j]]==0)
                {
                    count--;
                }
            }
            if(j-i+1 < k)
            {
                j++;
            }
            else{
                if(count==0)
                {
                    result.push_back(i);
                }
                if(mp.find(s[i]) != mp.end())
                {
                    mp[s[i]]++;
                    if(mp[s[i]]==1){
                        count++;
                    }
                }
                i++;
                j++;
            }
        }
        return result;
    }
};