class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> result;
        for(int i=0;i<expression.size();i++)
        {
            char c = expression[i];
            if(c == '+' || c == '-' || c == '*'){
                vector<int> left = diffWaysToCompute(expression.substr(0,i));
                vector<int> right = diffWaysToCompute(expression.substr(i+1));
                for(auto le:left)
                {
                    for(auto re: right)
                    {
                        if(c=='+')result.push_back(le+re);
                        else if(c=='-')result.push_back(le-re);
                        else if(c=='*')result.push_back(le*re);
                    }
                }

            }
        }
        if (result.empty()) {
        result.push_back(atoi(expression.c_str()));
    }
        return result;
    }
};