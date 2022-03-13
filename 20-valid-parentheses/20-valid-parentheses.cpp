class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='(' || s[i]=='[' || s[i]=='{')
            {
                char pu = (s[i]=='(')?')':((s[i]=='[')?']':'}');
                st.push(pu);                
            }
            if(!(st.empty()) && (s[i]==')' || s[i]==']' || s[i]=='}'))
            {
                if(st.top()==s[i])
                {
                    st.pop();
                }
                else
                {
                    return false;
                }
            }
            else if(st.empty() && (s[i]==')' || s[i]==']' || s[i]=='}'))return false;
        }
        if(st.empty())return true;
        return false;
    }
};