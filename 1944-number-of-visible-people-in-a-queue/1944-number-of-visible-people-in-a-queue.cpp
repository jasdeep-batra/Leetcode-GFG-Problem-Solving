class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        vector<int> answer(heights.size(),0);
        stack<pair<int,int>> st;
        st.push({heights.back(),heights.size()-1});
        for(int i=heights.size()-2;i>=0;i--)
        {
            int cnt = 0;
            while(!st.empty() && heights[i]>st.top().first)
            {
                cnt++;
                st.pop();
            }
            if(!st.empty())
            {
                answer[i] = cnt+1;
            }
            else
            {
                answer[i] = cnt;
            }
            st.push({heights[i],i});
        }
        return answer;
    }
};