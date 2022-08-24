class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<=0)return false;
        auto ans = log10(n)/log10(3);
        if(ans-int(ans)==0){
            return true;
        }
        return false;
    }
};