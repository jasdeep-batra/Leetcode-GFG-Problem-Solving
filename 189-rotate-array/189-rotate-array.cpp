class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int i = 0,mem = nums[0],cnt=0;
        int j = 0;
        while(cnt<nums.size())
        {
            
            do{
                int mem2 = nums[(j+k)%nums.size()];
                nums[(j+k)%nums.size()] = mem;
                mem = mem2;
                j = (j+k)%nums.size();
                cnt++;
            }while(j!=i);
            i++;
            mem = nums[i];
            j=i;
            
        }
        //nums[j] = mem;
    }
};