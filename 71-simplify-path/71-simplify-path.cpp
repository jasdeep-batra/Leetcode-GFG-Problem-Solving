class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        int i = 0;
        string c;
        for(int i=0;i<path.size();i++)
        {
            if(path[i]=='/')
            {
                continue;
            }
            string c;
            while(i<path.size() && path[i]!='/')
            {
                c+=path[i];
                i++;
            }
            if(c==".")
            {
                continue;
            }
            else if(c=="..")
            {
                if(!st.empty())
                {
                    st.pop();
                }
            }
            else
            {
                st.push(c);
            }
        }
        if(st.empty())return "/";
        string ans;
        while(!st.empty())
        {
            ans = '/' + st.top() + ans;
            st.pop();
        }
        return ans;
    }
};