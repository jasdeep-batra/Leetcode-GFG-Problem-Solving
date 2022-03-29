class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // It's is similar to linked list cycle
        int slow = nums[slow];  // slow = slow->next;
        int fast = nums[nums[fast]]; // fast = fast->next->next;
        while(slow!=fast)
        {
            slow = nums[slow];
            fast = nums[nums[fast]];            
        }
        fast = 0;
        while(fast!=slow)
        {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};