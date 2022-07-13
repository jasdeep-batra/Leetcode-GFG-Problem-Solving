/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        //BFS
        if(!root)return root;
        queue<pair<Node*,int>> q;
        queue<pair<Node*,int>> nq;
        q.push({root,0});
        while(!q.empty())
        {
            auto curr = q.front().first;
            auto lev = q.front().second;
            nq.push({curr,lev});
            q.pop();
            if(curr->left)
            {
                q.push({curr->left,lev+1});
            }
            if(curr->right)
            {
                q.push({curr->right,lev+1});
            }
        }
        auto ne = new Node(-1);
        ne->left = nq.front().first;
        auto f = nq.front().first;
        auto rut = nq.front().first;
        int l = nq.front().second;
        nq.pop();
        while(!nq.empty())
        {
            if(nq.front().second==l)
            {
                f->next = nq.front().first;
            }
            else{
                f->next = nullptr;
            }
            f = nq.front().first;
            l =nq.front().second;
            nq.pop();
        }
       // cout<<"working";
        return root;        
    }
};