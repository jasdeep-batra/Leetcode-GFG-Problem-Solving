class Solution {
public:
    int getprice(vector<int>& price, vector<int>& needs)
    {
        int maximum_price = 0;
        for(int i=0;i<price.size();i++)
        {
            maximum_price += price[i]*needs[i];
        }
        return maximum_price;
    }
    void offers(vector<int>& offer, vector<int>& needs, int remove)
    {
        if(remove==0)
        {
            for(int i=0;i<needs.size();i++)
            {
                needs[i]-=offer[i];
            }            
        }
        else
        {
            for(int i=0;i<needs.size();i++)
            {
                needs[i]+=offer[i];
            }
        }
    }
    bool isnegative(vector<int>& needs)
    {
        for(auto i: needs)
        {
            if(i<0)return false;
        }
        return true;
    }
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int maximum_price = getprice(price,needs);
        int now_price = 0;
        for(auto i: special)
        {
            offers(i,needs,0);
            if(isnegative(needs)==true)
            {
                int now_price = i.back() + shoppingOffers(price,special,needs);
                maximum_price = min(maximum_price,now_price);
                
            }
            offers(i,needs,1);
        }
        return maximum_price;      
    }
};