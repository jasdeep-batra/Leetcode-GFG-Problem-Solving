class Solution {
public:
    int minAddToMakeValid(string s) {
        int add = 0;
        int check = 0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(')
            {
                check++;
            }
            else if(s[i]==')')
            {
                if(check==0)
                {
                    add++;
                }
                else if(check>0)
                {
                    check--;
                }
            }
        }
        return check+add;
    }
};