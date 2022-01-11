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
        int carry = 0,count1=0,count2=0;
        while(p1!=NULL && p2!=NULL)
        {            
            int sum = p1->val+p2->val+carry;
            if(sum>9)
            {
                carry = 1;
            }
            else
            {                
                carry = 0;
            }
            p2->val = sum%10;
            p1->val = sum%10;
            if(p1->next==NULL && p2->next==NULL)
            {cout<<"working1"<<endl;tem = p1;}
           
            p1 = p1->next;
            p2 = p2->next; 
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
             return l1;
        }
        if(p1==NULL && p2!=NULL)
        {
            count1 =1;
            p1 = p2;
        }
        while(p1!=NULL)
        {   int sum = p1->val+carry;
            p1->val=sum%10;
            if(sum>9)carry=1;
            
            else carry=0;
            if(p1->next==NULL && carry==1)
            {
                ListNode* c = new ListNode(1); 
                p1->next = c;
                p1 = p1->next;
            }
            p1 = p1->next;            
        }
        
        if(count1==1) return l2;
        return l1;
    }
};