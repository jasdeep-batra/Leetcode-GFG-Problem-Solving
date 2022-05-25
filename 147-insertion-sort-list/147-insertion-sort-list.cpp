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
        auto i = head->next;
        head->next = nullptr;
        while(i)
        {
            auto ni = i->next;
            auto j = head;
            if(j->val > i->val)
            {
                i->next = j;
                head = i;
            }
            else
            {
                while(j && j->next && j->next->val < i->val)
                {
                    j = j->next;
                }
                i->next = j->next;
                j->next = i;
            }
            i = ni;
        }
        return head;
    }
};