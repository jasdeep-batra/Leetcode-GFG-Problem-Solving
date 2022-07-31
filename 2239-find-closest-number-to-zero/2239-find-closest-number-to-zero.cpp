class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        //sort(nums.begin(),nums.end());
        pair<int,int> p;
        p.first = (abs(nums[0])-0);
        p.second = nums[0];
                       
        for(int i=1;i<nums.size();i++)
        {
            int diff = abs(nums[i])-0;
            if((diff==p.first))
            {
                if(p.second>0 && nums[i]<0){
                    continue;
                }
                else{
                    p.second = nums[i];
                }
            }
            if(diff<p.first)
            {
                p.first = diff;
                
                p.second = nums[i];
                
            }
        }
        return p.second;
    }
};