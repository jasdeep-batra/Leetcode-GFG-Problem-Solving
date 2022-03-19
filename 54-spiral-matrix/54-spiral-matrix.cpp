class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int top = 0; // top
        int bottom = matrix.size(); // bottom
        int left = 0; // left
        int right = matrix[0].size(); // right
        vector<int>result;
        while(left<right && top<bottom)
        {
            for(int i=left;i<right;i++)
            {
                result.push_back(matrix[top][i]);
            }
            top++;
            for(int i=top;i<bottom;i++)
            {
                result.push_back(matrix[i][right-1]);
            }
            right--;
            if(left<right && top<bottom)
            {                
                for(int i = right-1;i>=left;i--)
                {
                    result.push_back(matrix[bottom-1][i]);
                }
                bottom--;
                for(int i=bottom-1;i>=top;i--)
                {
                    result.push_back(matrix[i][left]);
                }
                left++;
            }
            else break;
            
        }
        return result;
    }
};