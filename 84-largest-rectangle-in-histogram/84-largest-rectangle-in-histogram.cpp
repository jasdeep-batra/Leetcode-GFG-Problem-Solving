class Solution {
public:
    vector<int> nearleft(vector<int> heights)  // smallest
    {
        vector<int> nsl;
        stack<pair<int,int> > s;
        for(int i=0;i<heights.size();i++)
        {
            int index = -1;
            while(!(s.empty()))
            {
                if(s.top().first >= heights[i])
                {
                    s.pop();
                }
                else{
                    index = s.top().second;
                    break;
                }
            }            
            nsl.push_back(index);
            s.push(make_pair(heights[i],i));
        }
        return nsl;
    }
    vector<int> nearright(vector<int> heights) // smallest
    {
        vector<int> nsr;
        stack<pair<int,int> > s;
        for(int i=heights.size()-1;i>=0;i--)
        {
            int index = heights.size();
            while(!(s.empty()))
            {
                if(s.top().first >= heights[i])
                {
                    s.pop();
                }
                else{
                    index = s.top().second;
                    break;
                }
            }           
            
            nsr.push_back(index);
            s.push(make_pair(heights[i],i));
        }
        reverse(nsr.begin(),nsr.end());
        return nsr;
    }
    int largestRectangleArea(vector<int>& heights) {
        vector<int> nsl;
        vector<int> nsr;
        nsl = nearleft(heights);
        nsr = nearright(heights);
        int area = INT_MIN;
        for(int i=0;i<nsl.size();i++)
        {
            int curarea = heights[i]*(nsr[i]-nsl[i]-1);
            area = max(area,curarea);
        }
        return area;
    }
};