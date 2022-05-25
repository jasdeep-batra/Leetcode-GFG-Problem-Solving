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
    ListNode* insertionSortList(ListNode* head) {
        for(auto i = head;i;i=i->next)
        {
            for(auto j = head;j!=i;j=j->next)
            {
                if(j->val >i->val)
                {
                    swap(j->val,i->val);
                }
            }
        }
        return head;
    }
};