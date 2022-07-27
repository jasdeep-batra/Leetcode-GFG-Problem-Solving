class Solution {
public:
    string getHint(string secret, string guess) {
        map<char,int> mp;
        for(int i=0;i<secret.size();i++)
        {
            mp[secret[i]]++;
        }
        int a=0,b=0;
        for(int i=0;i<guess.size();i++)
        {
            if(secret[i]==guess[i])
            {
                mp[guess[i]]--;
                a++;
            }
        }
        for(int i=0;i<guess.size();i++)
        {
            if(secret[i]!=guess[i])
            {
                if(mp.find(guess[i])!=mp.end() && mp[guess[i]]>0)
                {
                    b++;
                    mp[guess[i]]--;
                }
                
            }
        }
        string res = to_string(a)+'A'+to_string(b)+'B';
        return res;
    }
};