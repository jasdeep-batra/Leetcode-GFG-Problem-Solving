class Solution {
public:
    int minOperations(int n) {
        //odd array
        // drr = [1,3,5,7,9]; 3 3 5 7 7 4 3 5 7 
        //1 1 3 4 6 9 12 16 20 25
        // average will gonna be n;
        int sum = 0;
        for(int i=0;i<n/2;i++)
        {
            sum+=(n - (2*i+1));
        }
        
        return sum;
    }
};