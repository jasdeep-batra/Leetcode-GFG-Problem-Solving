class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        if(intervals.size()==0)
        {
            result.push_back(newInterval);
            return result;
        }
        int ll = intervals[0][0];
        int ul = intervals[0][1];
        int x = newInterval[0];
        int y = newInterval[1];
        int pass = 0; int done = 0;
        vector<int> temp;
        for(int i=0;i<intervals.size();i++)
        {
            if(done==0 && pass==1 && y<intervals[i][0])
            {
                temp.push_back(y);
                result.push_back(temp);
                done = 1;
                pass = 0;
            }
            if(done==1)
            {
                vector<int> rem = {intervals[i][0],intervals[i][1]};
                result.push_back(rem);
                continue;
            }
            if(pass==0)
            {
                temp.clear();
            }
            if(pass==0 && (x>=intervals[i][0] && y<=intervals[i][1]))
            {
                return intervals;
            }
            
            if(x > intervals[i][1])
            {
                temp.push_back(intervals[i][0]);
                temp.push_back(intervals[i][1]);// incomplete
                result.push_back(temp); 
                temp.clear();
                continue;
            }
            if(x<=intervals[i][1])
            {        
                ul = max(ul,intervals[i][1]);
                if(pass==0 && x<intervals[i][0])
                {
                    temp.push_back(x);
                    if(y<intervals[i][0])
                    {
                        temp.push_back(y);
                        result.push_back(temp);
                        done=1;
                        pass=0;
                        vector<int> cur = {intervals[i][0],intervals[i][1]};
                        result.push_back(cur);
                        continue;
                    }
                }
                else if(pass==0 && x>=intervals[i][0]) 
                {
                    temp.push_back(intervals[i][0]);
                }
                if(y>=ul)
                {
                    pass = 1;
                }
                else if(y<=intervals[i][1])
                {
                    temp.push_back(intervals[i][1]);
                    result.push_back(temp);
                    pass = 0;
                    done = 1;
                }
            }
        }
        if(done==0)
        {
            if(temp.empty()==false)
            {
                temp.push_back(y);
                result.push_back(temp);    
            }
            else result.push_back(newInterval);
            return result;
        }
        return result;
    }
};