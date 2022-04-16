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
    void reorderList(ListNode* head) {
        //there are so many methods but out of them we have to choose omptimised one.
        stack<ListNode*> st;
        //queue<ListNode*> qt;
        ListNode* ptr = head;
        while(ptr!=nullptr)
        {
            st.push(ptr);
            ptr=ptr->next;            
        }
        // while(!st.empty())
        // {
        //     cout<<st.top()->val<<" " ;st.pop();
        // }
        ListNode* pt = head;
        int i;
        int siz = st.size();
        (siz%2==0)?i=1:i=0;
        while(i<siz/2)
        {
            ListNode* stno = st.top();//4 3
            st.pop();
            //stno->next = NULL;
            ListNode* temp = pt->next; // 3
            pt->next = stno;
            stno->next = temp;
            pt = temp;
            st.top()->next=NULL;            
            i++;
        }
    }
};