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
        if(list1==NULL && list2==NULL) return NULL;
        
            else if(list1==NULL)
            {
                return list2;
            }
            else if(list2==NULL) return list1;
        ListNode* h2 = NULL;
            ListNode* h1 = NULL;
        if(list1->val >= list2->val)
        {
        h2 = list2;
        h1 = list1;    
        }
        else
        {
             h2 = list1;
            h1 = list2;  
        }
        while(h2!=NULL && h1!=NULL)
        {
            ListNode* p2 = NULL;
            while(h2!=NULL)
            {
                if(h1->val >= h2->val)
                {
                    p2 = h2;
                    h2 = h2->next;
                }
                else
                {
                    break;
                }
            }
                p2->next = h1;
                ListNode* te = h2;
                h2 = h1;
                h1 = te;  
        }
        if(list1->val >= list2->val) return list2;
        
        return list1;
    }
};