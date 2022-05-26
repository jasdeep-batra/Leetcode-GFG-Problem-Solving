class Solution {
public:
    void set(string& s)
    {
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='#')
            {
                int j = i;
                s[i] = '-';
                while(j>=0 && s[j]=='-')
                {
                    j--;
                }
                if(j>=0)s[j] = '-';
            }
        }
        s.erase(remove(s.begin(), s.end(), '-'), s.end());
    }
    bool backspaceCompare(string s, string t) {
        //naive aaproach is where u can use stack
        set(s);set(t);
        cout<<s<<" "<<t;
        if(s==t)return true;
        
        return false;
        
    }
};