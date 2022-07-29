class Solution {
public:
    int nthUglyNumber(int n) {
    //using dynamic programming
        vector<int> arr(n,1);
        int i=0,j=0,k=0,two=2,three=3,five=5;
        int small_ugly_no = 1;
        for(int c=1;c<n;c++)
        {
             small_ugly_no = min(two,min(three,five));
            arr[c] = small_ugly_no;
            if(two==small_ugly_no)
            {
                i++;
                two = arr[i]*2;
            }
            if(three==small_ugly_no)
            {
                j++;
                three = arr[j]*3;
            }
            if(five==small_ugly_no)
            {
                k++;
                five = arr[k]*5;
            }
        }
        return arr[n-1];
    }
};