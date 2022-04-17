class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        char sign = '+';
        int num = 0;
        for(int i=0;i<s.size();i++)
        {
            if(isdigit(s[i]))
            {
                num = 10*num + int(s[i]-'0'); 
                cout<<num<<endl;
            }
            if(!isdigit(s[i]) && !isspace(s[i]) || i==s.size()-1)
            {
                if(sign=='+')
                {
                    st.push(num);
                }
                else if(sign=='-')
                {
                    st.push(-num);
                }
                else
                {
                    int fa = 0;
                    if(sign=='*')
                    {
                        fa = st.top()*num; 
                    }
                    else if(sign=='/')
                    {
                        fa = st.top()/num; 
                    }
                    cout<<fa<<endl;
                    st.pop();
                    st.push(fa);
                }
                num = 0;
                sign = s[i];
            }
        }
        int ans=0;
        while(!st.empty())
        {
            ans+=st.top();
            st.pop();
        }
        return ans;
    }
};