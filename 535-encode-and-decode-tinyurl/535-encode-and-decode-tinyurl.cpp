class Solution {
public:
    
    // Encodes a URL to a shortened URL.
    map<string,string> mp;
    const string chars = "1234567890abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    string getlink()
    {
        string code="";
        for(int i=0;i<6;i++)
        {
            code+=chars[rand()%62];
        }
        return "http://tinyurl.com/"+code;
    }
    string encode(string longUrl) {
        string code = getlink();
        while(mp.find(code)!=mp.end())
        {
            code = getlink();
        }
        mp[code] = longUrl;
        return code;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        return mp[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));