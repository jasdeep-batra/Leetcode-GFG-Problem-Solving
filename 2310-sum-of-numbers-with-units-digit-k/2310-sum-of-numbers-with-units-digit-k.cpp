class Solution {
public:
    int minimumNumbers(int num, int k) {
        if(num==0)return 0;
        if(k%2==0 && (num%10)%2!=0)return -1;
        int unit_place = num%10,n=1;
        for(int i=1;i<=10;i++)
        {
            if((k*i)%10==num%10 && i*k<=num){
                return i;
            }
        }
        
        //if(n*k<=num)return n;
        return -1;
    }
};