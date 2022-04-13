class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> mat(n,vector<int>(n,0));
        int top = 0, left = 0, bottom = n-1, right = n-1,count=1;
        while(top<=bottom && left<=right)
        {
            for(int i=left;i<=right;i++)
            {
                mat[top][i] = count++; 
            }
            for(int i=top+1;i<=bottom;i++)
            {
                mat[i][right] = count++; 
            }
            for(int i=right-1;i>=left;i--)
            {
                mat[bottom][i] = count++; 
            }
            for(int i=bottom-1;i>top;i--)
            {
                mat[i][left] = count++; 
            }
            top++;
            right--;
            bottom--;
            left++;
        }
        
        return mat;
    }
};