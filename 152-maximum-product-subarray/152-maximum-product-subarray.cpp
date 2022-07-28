class Solution {
public:
    int maxProduct(vector<int>& nums) {
        //so here we will store 2 datas maximum and minimum product;
        long maxx = INT_MIN;
        long minn = INT_MAX,res=INT_MIN;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]<0)
            {
                //maxx = max(maxx,minn*nums[i]);
                swap(maxx,minn);
                
            }
            maxx = max((long)nums[i],maxx*nums[i]); 
            minn = min((long)nums[i],minn*nums[i]);                
            res = max(res,maxx);
                
        }
        return res;
    }
};