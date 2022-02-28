class Solution {
public:
vector<int> result;
void recursion(vector<vector<int>> grid, int i, int j, int sum)
{
if(i<0 && j==grid[0].size())
{
result.push_back(sum);
cout<<sum<<endl;
return;
}
if(i<grid.size() && j<grid[0].size())
{
recursion(grid,i,j+1,sum+grid[i][j]);
recursion(grid,i+1,j,sum+grid[i][j]);
}
if(j==grid.size())
{
recursion(grid,i+1,j,sum+grid[i][j-1]);
}
if(i==grid.size())
{
recursion(grid,i,j+1,sum+grid[i-1][j]);
}
}
int minPathSum(vector<vector<int>>& grid) {
recursion(grid,0,0,0);
sort(result.begin(),result.end());
return result.front();
}
};