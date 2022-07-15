class Solution {
public:
    void solve(vector<vector<int>>& heights,vector<vector<bool>>& visit, int i, int j)
    {
        int m = heights.size();
        int n = heights[0].size();
        visit[i][j] = true;
        if( i-1>=0 &&visit[i-1][j] != true &&  heights[i-1][j] >= heights[i][j]) 
        {
                 solve(heights,visit,i-1,j);
            
        }
        if(i+1<heights.size() &&visit[i+1][j] != true&& heights[i+1][j] >= heights[i][j])
        {
                 solve(heights,visit,i+1,j);
            
        }
        if(j-1>=0 &&visit[i][j-1] != true&& heights[i][j-1] >= heights[i][j]) 
        {
            
                 solve(heights,visit,i,j-1);
                        
        }
        if(j+1<heights[0].size() &&visit[i][j+1] != true && heights[i][j+1] >= heights[i][j])
        {
                 solve(heights,visit,i,j+1);
        }
        // if (i-1 >= 0 && visited[i-1][j] != true && matrix[i-1][j]>=matrix[i][j])
        //     solve(matrix, visited, i-1, j);
        // //down
        // if (i+1 < m && visited[i+1][j] != true && matrix[i+1][j]>=matrix[i][j])
        //     solve(matrix, visited, i+1, j);
        // //left
        // if (j-1 >= 0 && visited[i][j-1] != true && matrix[i][j-1]>=matrix[i][j])
        //     solve(matrix, visited, i, j-1);
        // //right
        // if (j+1 <n && visited[i][j+1] != true && matrix[i][j+1]>=matrix[i][j])
        //     solve(matrix, visited, i, j+1);
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> result;
        vector<vector<bool>> atlantic(heights.size(),vector<bool>(heights[0].size(),false));
        vector<vector<bool>> pacafic(heights.size(),vector<bool>(heights[0].size(),false));
        for(int i=0;i<heights.size();i++)
        {
            solve(heights,pacafic,i,0);
            solve(heights,atlantic,i,heights[0].size()-1);
        }
        for(int i=0;i<heights[0].size();i++)
        {
            solve(heights,pacafic,0,i);
            solve(heights,atlantic,heights.size()-1,i);
        }
        for(int i=0;i<heights.size();i++)
        {
            for(int j=0;j<heights[0].size();j++)
            {
                if(pacafic[i][j] && atlantic[i][j])
                {
                    vector<int> t;
                    t.push_back(i);
                    t.push_back(j);
                    result.push_back(t);
                }
            }
        }
        return result;
    }
};