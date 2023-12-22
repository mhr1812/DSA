class Solution {
public:
    int strStr(string haystack, string needle) {
        int h = haystack.size();
        int n=0;
        for(int i=0;i<h;i++){
            if(haystack[i]==needle[n])
                n++;
            else{
                i = i-n;
                n=0;
            }
            if(n==needle.size())
                return i-n+1;
        }
        return -1;
    }
};