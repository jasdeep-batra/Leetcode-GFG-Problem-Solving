class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        vector<int> nums = {a,b,c};
        vector<int> result(2,0);
        sort(nums.begin(),nums.end());
        int mini=0, maxi=0;
        if((nums[0]+1==nums[1]) && (nums[1]+1==nums[2])){
            //result = {mini.maxi};
            return result;
        }
        if(nums[1]-nums[0]>1 && nums[2]-nums[1]>1){
            maxi += max(maxi,nums[1]-nums[0]+nums[2]-nums[1]-2);
            if(nums[1]-nums[0]==2 || nums[2]-nums[1]==2)mini = 1;
            else mini = 2;
            result = {mini,maxi};
            return result;
        }
        else if(nums[1]-nums[0]>1){
            maxi = nums[1]-nums[0]-1;
            mini = 1;
            result = {mini,maxi};
            return result;
            
        }
        else if(nums[2]-nums[1]>1){
            maxi = nums[2]-nums[1]-1;
            mini = 1;
            result = {mini,maxi};
            return result;
            
        }
        else{
            return result;
        }
    }
};