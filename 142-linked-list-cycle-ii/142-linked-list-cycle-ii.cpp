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
    ListNode *detectCycle(ListNode *head) {
        ListNode* s = head;
        ListNode* f = head;
        if(head==NULL || head->next == NULL)return NULL;
        while(f->next!=NULL && f->next->next!=NULL)
        {
            f = f->next->next;
            s = s->next;
            if(f==s)
            {
                ListNode* c = head;
                while(c!=s)
                {
                    c=c->next;
                    s=s->next;
                }
                return s;
            }
        }
        return NULL;
    }
};