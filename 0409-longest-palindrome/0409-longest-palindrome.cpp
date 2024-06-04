class Solution {
public:
    int longestPalindrome(string s) {
        map<char,int> mp;
        for(auto i: s)
        {
            mp[i]++;
        }
        bool one = false;
        int ans = 0;

        for(auto i= mp.rbegin(); i!=mp.rend();i++)
        {
            // cout<<i->second<<endl;
            if((i->second)%2!=0)
            {
                if(one == false){
                    ans+=i->second;
                    one=true;
                }
                else ans+=(i->second-1);
            }
            else{
                ans+=i->second;
            }
        }
        return ans;
        
    }
};