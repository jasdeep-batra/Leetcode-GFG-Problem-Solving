class Solution {
public:
    void recursion(int& cnt,int n, int i)  //i = 1
    {
        if(n==0)
        {
            cnt++;
            return;
        }
        for(int ind=i;ind<=5;ind++)
        {
            recursion(cnt,n-1,ind);                
        }
    }
    int countVowelStrings(int n) {
        int cnt=  0;
        recursion(cnt,n,1);
        return cnt;
    }
};