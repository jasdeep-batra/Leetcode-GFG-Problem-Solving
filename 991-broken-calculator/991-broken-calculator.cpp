class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int res = 0;
        while(target>startValue)
        {
            if(target%2==0)
            {
                target/=2;
                res++;
                
            }
            else
            {
                target+=1;
                res++;
            }
        }
        return res + (startValue-target);
    }
    
};