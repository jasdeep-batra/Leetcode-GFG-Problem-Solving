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
    ListNode* swapPairs(ListNode* head) 
    {
        if(head==NULL || head->next==NULL)return head;
        ListNode* prev = nullptr;
        //prev->next = head;
        ListNode* curr = head;
        ListNode* ans = head->next;
        while(curr!=nullptr && curr->next!=NULL) // enter the condition;
        {
            ListNode* tem = curr->next;
            //cout<<tem->val<<endl;
            curr->next = tem->next;
            tem->next = curr;
            if(prev){
                prev->next = tem;
            }
            prev = curr; 
            curr = curr->next;
            //cout<<curr->val<<endl;
        }        
        return ans;
    }
};