class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int,int>> q;
        int total = 0;
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[0].size();j++)
            {
                if(grid[i][j]!=0)total++;
                if(grid[i][j]==2)
                {
                    q.push(make_pair(i,j));                    
                }
            }
        }
        int count = 0;
        int day = 0;
        cout<<q.front().first<<q.front().second<<endl;
        while(q.empty()==false)
        {
            int temp_count = q.size();
            count+=temp_count;
            for(int i=0;i<temp_count;i++)
            {
                int ii = q.front().first;
                int jj = q.front().second;
                q.pop();
                // ii-1,jj  /  ii,jj-1 / ii+1,jj / ii,jj+1
                if(ii-1>=0 && (grid[ii-1][jj]==1))
                {
                    grid[ii-1][jj] = 2;
                    q.push(make_pair(ii-1,jj));
                }
                if(ii+1<=grid.size()-1 && (grid[ii+1][jj]==1))
                {
                    grid[ii+1][jj] = 2;
                    q.push(make_pair(ii+1,jj));
                }
                if(jj-1>=0 && (grid[ii][jj-1]==1))
                {
                    grid[ii][jj-1] = 2;
                    q.push(make_pair(ii,jj-1));
                }
                if(jj+1<=grid[0].size()-1 && (grid[ii][jj+1]==1))
                {
                    grid[ii][jj+1] = 2;
                    q.push(make_pair(ii,jj+1));
                }
                                
            }  
            if(!(q.empty()))day++;
        }
        if(count==total)return day;
        return -1;        
    }
};