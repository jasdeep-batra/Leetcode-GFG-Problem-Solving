class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t num = 1;
        int i = 0;
        vector<int> arr(32,0);
        while(n)
        {
            int a = n & 1;
            arr[i++] = a;
            n = n>>1;
        }
        
        string ans;
        uint32_t fans = 0;
        for(int j=0;j<32;j++)
        {
            cout<<j;
            fans += pow(2,j)*arr[32-j-1];
        }
       // cout<<ans;
        return fans;
    }
};