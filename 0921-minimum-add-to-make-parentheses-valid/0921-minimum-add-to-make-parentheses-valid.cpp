class Solution {
public:
    int minAddToMakeValid(string s) {
        //stack
        int st = 0,x=0;
        for(char c:s){
            if(c=='('){
                st++;
            }
            else if(c==')'&&st>0){
                st--;
            }
            else{
                x++;
            }
        }
        return st+x;
    }
};