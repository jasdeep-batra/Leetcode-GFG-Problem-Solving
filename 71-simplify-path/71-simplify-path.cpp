class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        int i = 1;
        string c;
        while(i<path.size())
        {
            if(path[i]=='/')
            {
                if(!c.empty())st.push(c);
                c.clear();
            }
            else
            {
                c+=path[i];                
            }            
            i++;
        }
        //cout<<"wroking";
        if(!c.empty())st.push(c);
        stack<string> ss;
        string answer;
        // while(!st.empty())
        // {
        //     cout<<st.top()<<endl;st.pop();
        // }
        while(!st.empty())
        {
            cout<<"stack: "<<st.top()<<endl;
            if(st.top()=="..")
            {         
                if(st.size()==1)
                {
                    st.pop();
                    break;
                }
                st.pop();
                cout<<"if 1"<<endl;
                stack<string> nst;
                while(!st.empty() && (st.top()==".."||st.top()=="."))
                {
                        if(st.top()=="..")nst.push("..");
                        st.pop();
                }
                cout<<"if 2"<<endl;
                if(!st.empty())st.pop();
                else if(st.empty())
                {
                    cout<<"empty";
                    break;
                }
                while(!nst.empty()){
                    st.push(nst.top());
                    nst.pop();
                }
            }
            else if(st.top()==".")
            {
                st.pop();
            }
            else{
                ss.push(st.top());
                st.pop();
            }
        }
        if(ss.empty()){cout<<"true"<<endl;return "/";}
        while(!ss.empty())
        {
            answer+='/'+ss.top();ss.pop();
        }        
        if(answer[answer.size()-1]=='/')answer.erase(answer.size()-1,1);
        return answer;
    }
};