class Solution {
public:
    int countEven(int t) {
        //find pattern
        int sum = 0;
        int num  =t;
        while(num)
        {
            sum+=num%10;
            num/=10;
        }
        return (sum%2)?(t-1)/2:t/2;
    }
};