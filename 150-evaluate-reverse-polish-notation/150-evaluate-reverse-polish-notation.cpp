class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        //postfix
        stack<int> st;
        for(int i=0;i<tokens.size();i++)
        {
            if(tokens[i]!="+"&&tokens[i]!="-"&&tokens[i]!="*"&&tokens[i]!="/")
            {
                st.push(stoi(tokens[i]));
            }
            else
            {
                if(tokens[i]=="+")
                {
                    int f = st.top();
                    st.pop();
                    int l = st.top();
                    st.pop();
                    st.push(f+l);
                }
                else if(tokens[i]=="-")
                {
                    int f = st.top();
                    st.pop();
                    int l = st.top();
                    st.pop();
                    st.push(l-f);
                }
                else if(tokens[i]=="*")
                {
                    int f = st.top();
                    st.pop();
                    int l = st.top();
                    st.pop();
                    st.push(l*f);
                }
                else if(tokens[i]=="/")
                {
                    int f = st.top();
                    st.pop();
                    int l = st.top();
                    st.pop();
                    st.push(l/f);
                }
            }
        }
        int ans =0;
        while(!st.empty())
        {
            ans+=st.top();
            st.pop();
        }
        return ans;
    }
};