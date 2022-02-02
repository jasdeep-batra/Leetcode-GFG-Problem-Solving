class MinStack {
public:
    long long me;
    stack<long long> s;
    MinStack() {
        me = -1;
    }
    
    void push(long long val) {
        if(s.empty())
        {
            me = val;
            s.push(val);
        }
        else
        {
            if(val >= me)
            {
                s.push(val);
            }
            else
            {
                s.push(2*val - me);
                me = val;
            }
        }
    }
    
    void pop() {
        
        if(s.top() >= me)
        {
            s.pop();
        }
        else
        {
            me = 2*me - s.top();
            s.pop();
        }
    }
    
    int top() {
        if(s.empty())return -1;
        
        if(s.top() >= me)
        {
            return s.top();
        }
        else
        {
            return me;
        }
    }
    
    int getMin() {
        if(s.empty())return -1;
        return me;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */