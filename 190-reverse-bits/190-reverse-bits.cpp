class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t num = 0;
        int i = 0;
        int pi = 31;
        //vector<int> arr(32,0);
        while(n)
        {
            int a = n & 1;
           // arr[i++] = a;
            num+=pow(2,pi)*a;
            pi--;
            n = n>>1;
        }
        
        // string ans;
        // uint32_t fans = 0;
        // for(int j=0;j<32;j++)
        // {
        //     cout<<j;
        //     fans += pow(2,j)*arr[32-j-1];
        // }
        return num;
    }
};