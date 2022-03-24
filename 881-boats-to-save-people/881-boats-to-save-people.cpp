class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        if(people.front() > limit/2)return people.size();
        int i=0,j=people.size()-1;
        int boat = 0;
        while(i<=j)
        {
            if(people[i]+people[j] > limit)
            {
                boat++;
                j--;
            }
            else if(people[i]+people[j] <= limit)
            {
                boat++;
                i++;j--;
            }            
        }
        return boat;
    }
};