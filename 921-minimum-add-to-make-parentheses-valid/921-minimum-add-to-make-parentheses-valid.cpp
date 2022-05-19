class Solution {
public:
    int minAddToMakeValid(string s) {
        int l=0,c = 0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(')
            {
                l++;
            }
            if(s[i]==')' && l==0)
            {
                c++;
            }
            else if(s[i]==')')
            {
                l--;
            }
        }
        return l+c;
    }
};