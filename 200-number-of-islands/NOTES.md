{
m = bfs.front().first;
n = bfs.front().second;
if(dp[m][n]==1){bfs.pop();continue;}
dp[m][n] = 1;
if(m-1>=0 && grid[m-1][n]=='1')
{
if(dp[m-1][n]==0)bfs.push({m-1,n});
}
if(m+1<grid.size() && grid[m+1][n]=='1')
{
if(dp[m+1][n]==0)bfs.push({m+1,n});
}
if(n-1>=0 && grid[m][n-1]=='1')
{
if(dp[m][n-1]==0)bfs.push({m,n-1});
}
if(n+1<grid[0].size() && grid[m][n+1]=='1')
{
if(dp[m][n+1]==0)bfs.push({m,n+1});
}
bfs.pop();
}
answer++;
}
return answer;
}
};