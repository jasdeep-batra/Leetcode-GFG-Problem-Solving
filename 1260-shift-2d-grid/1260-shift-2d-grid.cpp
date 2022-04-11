class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        vector<vector<int>> answer(grid.size(),vector<int>(grid[0].size(),0));
        int m = grid.size(), n = grid[0].size();
        for(int i=0;i<grid.size();i++)
        {
            for(int j=0;j<grid[0].size();j++)
            {
                answer[(i+(j+k)/n)%m][(j+k)%n] = grid[i][j];
            }
        }
        return answer;
    }
};