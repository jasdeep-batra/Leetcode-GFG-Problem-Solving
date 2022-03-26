class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
       vector<int> result(triangle.size(), triangle[0][0]);
        for (unsigned int i = 1; i < triangle.size(); i++) 
        {
            for (int j = i; j >= 0; j--) 
            {
                if(j==0)
                {
                    result[j] = result[0] + triangle[i][j];
                }
                else if(j==i)
                {
                    result[j] = result[j-1] + triangle[i][j];
                }
                else
                {
                    result[j] = min( result[j-1],result[j] ) + triangle[i][j]; 
                }
            }
        }
        return *min_element(result.begin(), result.end());
    }
};