class node
{
public:
    int key;
    int value;
    node* next;
    node* prev;
    node(int k, int v)
    {
        next = NULL;prev = NULL;
        key = k; value = v;
    }    
};
class LRUCache {
public:
    int size;
    node* head;
    node* tail;
    map<int,node*> mp;
    LRUCache(int capacity) {
        size = capacity; 
        head = new node(-1,-1);
        tail = new node(-1,-1);
        head->next = tail;
        tail->prev = head;
    } 
    void remove_node(node* n)
    {
        node* n1 = n->prev;
        node* n2 = n->next;
        n1->next = n2;
        n2->prev = n1;
    }
    void add_front(node* n)
    {
        node* temp = head->next;
        head->next = n;
        n->prev = head;
        n->next = temp;
        temp->prev = n;
    }
    node* remove_last()
    {
        node* cur = tail->prev;
        node* t1 = cur->prev;
        t1->next = tail;
        tail->prev = t1;  
        return cur;
    }
    int get(int key) {
        if(mp.find(key)==mp.end())
        {
            return -1;
        }
        node* to_rem = mp[key];
        remove_node(to_rem);
        add_front(to_rem);
        return mp[key]->value;        
    }
    
    void put(int key, int value) {
        node* n = new node(key,value);
         if(mp.find(key)!=mp.end())
         {             
             node* to_rem = mp[key];            
             mp.erase(key);             
             remove_node(to_rem);
             add_front(n);
         }
        else
        {
            if(mp.size()>=size)
            {
                node* remvd = remove_last();
                mp.erase(remvd->key);                
                add_front(n);
            }
            else if(mp.size()<size)
            {
                add_front(n);
            }
        }
        mp[key] = n;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */