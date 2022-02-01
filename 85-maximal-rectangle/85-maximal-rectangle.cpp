class Solution {
public:
    int maxarea(vector<int> heights)
    {
        stack<int> s;
        int area = INT_MIN; int i=0;
        while(i<heights.size())
        {
            if(s.empty() || heights[i] > heights[s.top()])
            {
                s.push(i); // index;
                i++;
            }
            else
            {                
                int h = s.top();
                s.pop();int j;
                if(s.empty()) j = -1;
                else j = s.top();
                int nar = heights[h]*(i-j-1);
                cout<<"area: "<<nar<<endl;
                area = max(area,nar);                                             
            }            
        }
        while(!(s.empty()))
        {
            int h = s.top();
            s.pop();int j;
            if(s.empty()) j = -1;
            else j = s.top();
            area = max(area,heights[h]*(i-j-1));  
            cout<<"area: "<<heights[h]*(i-j-1)<<endl;
        }
        return area;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        int res = INT_MIN;
        vector<int> row(matrix[0].size(),0);
        
        for(int i=0;i<matrix.size();i++)
        {
            for(int j=0;j<matrix[0].size();j++)
            {
                if(matrix[i][j]=='1')
                    row[j]+=matrix[i][j]-'0';
                else if(matrix[i][j]=='0')
                {
                    row[j] = 0;
                }
            }
            res  = max(res,maxarea(row));
            
            cout<<"rs: "<<res<<endl;
        }
        //res = maxarea(row);
        return res;
    }
};