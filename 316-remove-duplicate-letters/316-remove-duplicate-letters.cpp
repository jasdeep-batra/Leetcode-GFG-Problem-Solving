class Solution {
public:
    string removeDuplicateLetters(string s) {
        map<char,int> mp;
        map<char,int> visit;
        string result;
        for(int i=0;i<s.size();i++)
        {
            mp[s[i]]++;    
            visit[s[i]] = 0;
        }
        stack<char> st;
        for(int i=0;i<s.size();i++)
        {            
            mp[s[i]]--;
            if(visit[s[i]]==1)continue;            
            while(!(st.empty()) && (s[i] < st.top()) && mp[st.top()] > 0)
            {
                visit[st.top()] = 0;
                st.pop();             
            }
            st.push(s[i]); 
            visit[s[i]] = 1;
        }
        while(!(st.empty()))
        {
            result.push_back(st.top());
            st.pop();
        }
        reverse(result.begin(),result.end());
        return result;
    }
};