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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* mh = NULL;
        ListNode* h1 = list1;
        ListNode* h2 = list2;
        if(list1==NULL && list2==NULL)
        {
            return NULL;
        }
        else if(list2==NULL)return list1;
        else if(list1==NULL)return list2;
        if(list1->val >=list2->val)
        {
            mh = list2;
            h2 = h2->next;
        }
        else
        {
            mh=list1;
            h1 = h1->next;
        }
        
        while(h2!=NULL && h1!=NULL)
        {
            if(h1->val  >=h2->val)
            {
                mh->next = h2;
                mh = mh->next;
                h2 = h2->next;
            }
            else
            {
                mh->next = h1;
                mh = mh->next;
                h1 = h1->next;
            }
        }
        while(h2!=NULL)
        {
            mh->next = h2;
            mh = mh->next;
            h2 = h2->next;
        }
        while(h1!=NULL)
        {
            mh->next = h1;
            mh = mh->next;
            h1 = h1->next;
        }
        if(list1->val >=list2->val)return list2;
        return list1;
    }
};