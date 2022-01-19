class Solution {
public:
    vector<string> result;
    void recur(string s, string res, int i)
    {
        if(i==s.size())
        {
            result.push_back(res);
            return;            
        }
        if(isdigit(s[i]))
        {
            recur(s, res+s[i],i+1);
        }
        else{char c = tolower(s[i]);
            recur(s,res+c,i+1);
            c = toupper(s[i]);
            recur(s,res+c,i+1);
            }
    }
    vector<string> letterCasePermutation(string s) {
        string res;
        recur(s,res,0);
        return result;
    }
};