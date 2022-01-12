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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL||head->next==NULL || k==0)return head;
        ListNode* f = new ListNode(-1);
        f->next = head;
        ListNode* s = f;ListNode* siz = head;
        int size = 0;
        while(siz!=NULL)
        {
            size++;
            siz=siz->next;
            
        }
        cout<<k%size;
        if(k%size==0)return head;
        for(int i=0;i<k%size;i++)
        {
            f=f->next;
        }
        while(f->next!=NULL)
        {
            f=f->next;
            s=s->next;
        }
        ListNode* nh = s->next;
        s->next = NULL;
        f->next = head;
        head = nh;
        return head;
    }
};