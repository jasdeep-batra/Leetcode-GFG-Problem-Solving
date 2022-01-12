/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* p1 = headA;
        ListNode* p2 = headB;
        map<ListNode* , int> mp;
        while(p1!=NULL)
        {
            mp[p1] = p1->val;
            p1 = p1->next;
        }
        while(p2!=NULL)
        {
            if(mp.find(p2)!=mp.end())
            {
                return p2;
            }
            else p2 = p2->next;         
        }
        return NULL;
        
    }
};