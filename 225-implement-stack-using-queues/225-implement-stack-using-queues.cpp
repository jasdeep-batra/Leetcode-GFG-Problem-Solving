class MyStack {
public:
    queue<int> q1;
    queue<int> q2;
    
    MyStack() {
        
    }
    
    void push(int x) {
        q1.push(x);
    }
    
    int pop() {
        if(empty())return -1;
        int size = q1.size();
        int i =0;
        while(i<size-1)
        {
            q2.push(q1.front());
            q1.pop();
            i++;
        }
        int ans = q1.front();
        q1.pop();
        q1=q2;
        queue<int> tg;
        q2 = tg;
        return ans;
    }
    
    int top() {
        if(empty())return -1;
        int size = q1.size();
        int i =0;
        while(i<size-1)
        {
            q2.push(q1.front());
            q1.pop();
            i++;
        }
        int ans = q1.front();
        q2.push(q1.front());
        q1.pop();
        q1=q2;
        queue<int> tg;
        q2 = tg;
        return ans;
    }
    
    bool empty() {
        if(q1.empty())return true;
        return false;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */