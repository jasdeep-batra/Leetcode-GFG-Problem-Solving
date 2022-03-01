class StockSpanner {
public:
    stack<pair<int,int>> s;
    int i = 0;
    StockSpanner() {
    }
    int next(int price) {
        int index = -1;
        while(!(s.empty()))
        {
            if(s.top().first <= price)
            {
                s.pop();
            }
            else
            {
                index = s.top().second;
                break;
            }
        }    
        int ans = i-index; 
        s.push({price,i++});
        return ans;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */