class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);string word;
        stack<string> st;
        while(ss>>word)
        {
            st.push(word);            
        }
        string result;
        while(st.empty()==false)
        {
            if(st.size()!=1)result+=st.top()+" ";
            else result+=st.top();
            st.pop();
        }
        return result;
    }
};