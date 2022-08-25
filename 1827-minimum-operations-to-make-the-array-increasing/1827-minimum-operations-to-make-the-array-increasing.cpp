class Solution {
public:
    int minOperations(vector<int>& nums) {
        stack<int> s;
        s.push(nums[0]);
        int operation = 0;
        for(int i=1;i<nums.size();i++)
        {
            if(s.top()>=nums[i])
            {
                operation+=(s.top()-nums[i]+1);
                s.push(s.top()+1);
            }
            else{
                s.push(nums[i]);
            }
        }
        return operation;
    }
};