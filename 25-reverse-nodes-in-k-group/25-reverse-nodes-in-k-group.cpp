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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* nhead = head;
        ListNode* curr = head;  
        queue<ListNode*> q;
        int count =0;
        cout<<"working"<<endl;
        ListNode* ch = curr;
        int count2 = 0,j=0;
        while(ch!=NULL)
        {
            count2++;
            ch=ch->next;
        }
        while(j<(count2/k))
        {
            q.push(curr);
            ListNode* prev = NULL;
            
            
            
            //if(count2<k)break;
            
            cout<<"working"<<endl;
            for(int i=0;i<k;i++)
            {
                ListNode* next = curr->next;
                curr->next = prev;
                prev = curr;
                curr = next;
            }
            cout<<"prev:"<<prev->val;
            count++;
            if(count>1)
            {
                q.front()->next = prev;
                q.pop();
            }
            else{
                nhead = prev;
            }
            j++;
        }
            if(!(q.empty())){
            q.front()->next = curr;
            q.pop();}
        return nhead;
    }
};