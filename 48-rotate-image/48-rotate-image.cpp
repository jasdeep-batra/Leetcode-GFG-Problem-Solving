class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int i = 0;
        int j = matrix.size()-1;
        int n = matrix.size();
        while(i<=j)
        {
            swap(matrix[i],matrix[j]);
            i++;j--;
        }
        int o = n-1;
        int m = 0;
        while(m<n)
        {
            cout<<"is it working"<<endl;
            if(o==m)
            {
                m++;
                o = n-1;
            }
            else
            {
                swap(matrix[m][o],matrix[o][m]);
                o--; 
            }
        }
    }
};