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
    ListNode* reverseList(ListNode* head) 
    {
        // //optimised //bruteforce
        // //2 pointer approach
        // ListNode* temp = head;
        // ListNode* tail = head;
        // stack<int> s;
        // while(tail!=NULL)
        // {
        //     s.push(tail->val);
        //     tail=tail->next;
        // }
        // while(!(s.empty()))
        // {
        //     temp->val = s.top();
        //     s.pop();
        //     temp = temp->next;
        // }
        // return head;
        
        
        ListNode* prev = NULL;
        ListNode* curr = head;
        while(curr!=NULL)
        {
            ListNode* new_curr = curr->next;
            //Below code is for Link break 
            curr->next = prev;
            prev = curr;
            curr = new_curr;            
        }
        return prev;
    }
};