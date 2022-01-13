/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* temp = head;
        Node* res = new Node(-1);
        Node* temp2 = res;
        map<Node*,Node*> mp;
        while(temp!=NULL)
        {
            Node* n = new Node(temp->val);
            temp2->next = n;
            mp[temp] = n;
            temp2 = temp2->next;
            temp = temp->next;
        }
        for(auto itr:mp)
        {
            itr.second->random = mp[itr.first->random];
        }
        return res->next;
    }
};