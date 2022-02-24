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
    ListNode* merge(ListNode* p2,ListNode* p1)
    {
        ListNode* temp = new ListNode(-1);
        ListNode* head = temp;
        while(p1!=NULL && p2!=NULL)
        {
            if(p1->val >= p2->val)
            {
                temp->next = p2;
                p2 = p2->next;
            }
            else
            {
                temp->next = p1;
                p1 = p1->next;
            }
            temp = temp->next;
        }
        if(p1!=NULL)
        {
            temp->next = p1;
            temp = temp->next;
        }
        if(p2!=NULL)
        {
            temp->next = p2;
            temp = temp->next;
        }
        return head->next;
    }
    ListNode* sortList(ListNode* head) {
        if(head==NULL || head->next==NULL)return head;
        ListNode* ptr1 = head;
        ListNode* ptr2 = head;
        while(ptr2->next!=NULL && ptr2->next->next!=NULL)
        {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next->next;
        }
        ListNode* head1 = head;
        ListNode* head2 = ptr1->next;
        ptr1->next = NULL;
        ListNode* l1 = sortList(head1);
        ListNode* l2 = sortList(head2);
        return merge(l1,l2);
    }
};