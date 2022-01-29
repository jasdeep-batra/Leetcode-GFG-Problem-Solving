class CustomStack {
public:
    vector<int> ourStack;
    int size;
    CustomStack(int maxSize){
        size = maxSize;
    }
    
    void push(int x) {
        if(ourStack.size()<size)
        {
            ourStack.push_back(x);
        }
    }
    
    int pop() {
        if(!(ourStack.empty()))
        {
            int temp = ourStack[ourStack.size()-1];
            ourStack.pop_back();
            return temp;
        }
        return -1;
    }
    
    void increment(int k, int val) {
        int i=0;
        while(i<ourStack.size())
        {
            if(i>=k)break;
            ourStack[i]+=val;
            i++;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */