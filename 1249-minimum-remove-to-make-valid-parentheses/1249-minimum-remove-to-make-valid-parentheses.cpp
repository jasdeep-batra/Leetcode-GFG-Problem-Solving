class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int i = 0,count = 0;
        string result;
        stack<pair<char,int>> st;
        while(i<s.size())
        {
            if(s[i]=='(')
            {
                result+=s[i];
                int ind = result.size()-1;
                st.push({s[i],ind});
            }
            else if(s[i]==')')
            {
                if(!(st.empty()))
                {
                    result+=s[i];
                    st.pop();
                }
            }
            else
            {
                result+=s[i];
            }
            i++;
        }
        cout<<result;
        int j = 0;
        while(st.empty()==false)
        {
            int ind = st.top().second;
            result.erase(result.begin()+ind);
            st.pop();
        }
        return result;
    }
};