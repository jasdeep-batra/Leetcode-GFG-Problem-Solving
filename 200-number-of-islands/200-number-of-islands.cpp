class Solution {
public:
    void bfs(vector<vector<char>>& grid, int i, int j)
    {
        if(i<0 || j<0 || i>=grid.size() || j>=grid[0].size())return;
        if(grid[i][j]=='0' || grid[i][j]=='2')return;
        grid[i][j] = '2';
        bfs(grid,i-1,j);
        bfs(grid,i+1,j);
        bfs(grid,i,j-1);
        bfs(grid,i,j+1);
    }
    int numIslands(vector<vector<char>>& grid) {
        int count = 0,answer = 0; 
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[0].size();j++)
            {
                if(grid[i][j]=='1')
                {                    
                    bfs(grid,i,j);
                    answer++;
                }
            }
        }
        return answer;
    }
};