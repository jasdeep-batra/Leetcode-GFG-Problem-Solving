class Solution {
public:
    int minDeletions(string s) {
        sort(s.begin(),s.end());
        map<int,char> mp;
        int i=0,j=1,deletion = 0;
        while(i<s.size())
        {
            if(j<s.size() && s[i]==s[j])
            {
                j++;
            }
            if(j==s.size() || s[i]!=s[j])
            {
                int occurance = j-i;
                while(mp.find(occurance)!=mp.end())
                {
                    occurance--;
                    deletion++;
                }
                if(occurance!=0)mp[occurance] = s[i];
                i = j;
                j++;
            }
        }
        return deletion;
    }
};