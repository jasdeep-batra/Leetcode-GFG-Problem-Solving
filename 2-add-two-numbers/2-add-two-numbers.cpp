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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* p1 = l1;
        ListNode* p2 = l2;
        ListNode* tem = NULL;
        int s1=0, s2=0,carry = 0,count1=0,count2=0;
        while(p1!=NULL || p2!=NULL)
        {            
            s1 = (p1)?p1->val:0;
            s2 = (p2)?p2->val:0;
            int sum = s1+s2+carry;
            // if(sum>9)
            // {
            //     carry = 1;
            // }
            // else
            // {                
            //     carry = 0;
            // }
            carry = sum/10;
            if(p1)
            {
                p1->val = sum%10;
                count1++;
                if(p1->next==NULL)tem = p1;
                p1 = p1->next;
            }
            if(p2)
            {
                p2->val = sum%10;
                count2++;
                if(p2->next==NULL)tem = p2;
                p2 = p2->next; 
            }
        }
        //cout<<"working"<<endl;
        if(p1==NULL && p2==NULL)
        {
            cout<<"working"<<endl;
            if(carry==1)
            {ListNode* c = new ListNode();
             c->val = 1;
            tem->next = c;
             cout<<"workingcv"<<endl;
            }
        }
        if(count1>count2) return l1;
        return l2;
    }
};