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
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==nullptr)return head;
        ListNode* slow = head;
        ListNode* fast = head->next;
        ListNode* prev = new ListNode(0,head);
        ListNode* start = prev;
        bool flag = false;
        while(fast)
        {
            if(flag==false && slow->val!=fast->val)
            {
                prev = slow;
                slow = slow->next;
                fast = fast->next;
            }
            else if(flag==true && slow->val!=fast->val)
            {
                prev->next = fast;
                slow = fast;
                fast = fast->next;
                flag = false;
            }
            else if(slow->val==fast->val)
            {
                fast = fast->next;
                flag = true;
            }
        }
        if(flag==true)
        {
            prev->next = fast;
        }
        return start->next;
    }
};