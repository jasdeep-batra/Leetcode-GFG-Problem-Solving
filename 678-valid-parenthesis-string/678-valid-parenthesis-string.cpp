class Solution {
public:
    bool checkValidString(string s)
    {
        int cnt = 0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]==')')cnt--;
            else cnt++;
            if(cnt<0)return false;
        }cnt=0;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(s[i]=='(')cnt--;
            else cnt++;
            if(cnt<0)return false;
        }
        return true;
    }
};