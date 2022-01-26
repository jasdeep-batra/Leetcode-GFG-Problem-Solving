class Solution {
public:
    int counfun(vector<vector<int>>& matrix, int target)
    {
        int i = 0,count=0;
        int j = matrix[0].size()-1;
        while(i<matrix.size() && j>=0)
        {
            if(matrix[i][j] > target)
            {
                j--;
            }
            else{
                count = count + j +1;
                i++;
            }
        }
        return count;
    }
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int first = matrix[0][0];
        int last = matrix[n-1][n-1];
        //int count = 0,ans=-1;
        while(first<last)
        {
            int mid = first + (last-first)/2;
            int count = counfun(matrix,mid);
            if(count<k)
            {
                first = mid+1;
            }
            else
            {
                last = mid;
            }
        }
        return first;
    }
};