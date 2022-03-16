class Solution {
public:
    vector<string> split(string s)
    {
        vector<string> result;
        string t;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='.')
            {
                result.push_back(t);
                t.clear();
            }
            else{
                t+=s[i];
            }
        }
        result.push_back(t);
        return result;
    }
    int compareVersion(string version1, string version2) {
        //split the string 
        // to convert the string into integer
        vector<string> ver1 = split(version1);
        vector<string> ver2 = split(version2);
        int size = max(ver1.size(),ver2.size());
        int i = 0;        
        while(i<size)
        {
            int a = (i<ver1.size())?stoi(ver1[i]):0;
            int b = (i<ver2.size())?stoi(ver2[i]):0;
            //cout<<"a: "<<a<<" ; b: "<<b<<endl;
            if(a==b)
            {
                i++;
            }
            if(a>b)
            {
                return 1;
            }
            if(b>a)
            {
                return -1;
            }
        }
        return 0;
    }
};