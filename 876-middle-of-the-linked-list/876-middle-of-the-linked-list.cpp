/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* tail = head;
        ListNode* mid = head;
        int count = 0;
        int i =0;
        //count+1 = size
        while(tail!=NULL)
        {
            count++;
            
            while(i<(count/2))
            {
                if(count%2==0)mid = mid->next;
                i++;
            }
            tail = tail->next;            
        }
        return mid;
    }
};