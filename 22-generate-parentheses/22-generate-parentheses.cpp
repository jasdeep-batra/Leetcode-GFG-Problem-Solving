class Solution {
public:
    vector<string> result;
    void parent(int open, int close, string res)
    {
        if(open==0 && close==0)
        {
            result.push_back(res);
            return;
        }
        if(close==open)
        {
            char c = '(';
            parent(open-1,close,res+c);
        }
        else{
            char c = '(';char d =')';
            if(open!=0) 
            {
                parent(open-1,close,res+c);
            }
            parent(open,close-1,res+d);
        }
    }
    vector<string> generateParenthesis(int n) {
        string res;
        parent(n,n,res);
        return result;
    }
};