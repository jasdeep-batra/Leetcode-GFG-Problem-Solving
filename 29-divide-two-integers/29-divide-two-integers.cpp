class Solution {
public:
    int divide(int dividend, int divisor) {
        //base conditions
        if(dividend==INT_MIN && divisor==-1)
        {
            return INT_MAX;
        }
        if(dividend==INT_MAX && divisor==1)return INT_MAX;
        int sign = 1;
        if(dividend<0 || divisor<0)
        {
            if(dividend<0 && divisor<0)
            {
                sign = 1;
            }
            else{
                sign = -1;
            }
        }
        long dividen = abs((long)dividend);
        long diviso = abs((long)divisor);
        long ans=0;
        while(dividen>=diviso)
        {
            long newdivisor = diviso;
            long a = 1;
            while(dividen>=(newdivisor<<1))
            {
                newdivisor<<=1;
                a<<=1;
            }
            dividen-=newdivisor;
            ans+=a;
        }
        return ans*sign;
    }
};