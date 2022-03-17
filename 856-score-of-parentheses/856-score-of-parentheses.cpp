class Solution {
public:
    int scoreOfParentheses(string s) {
        int count = 0;
        int score = 0,i=0;
        while(i<s.size())
        {
            if(s[i]=='(')
            {
                count++;i++;
            }
            else if(s[i]==')')
            {
                if(count==1)
                {
                    score++;count--;i++;
                }
                else{
                    score+=pow(2,count-1);
                    while(s[i]==')'){count--;i++;}
                }
            }
                
        }
        return score;
    }
};