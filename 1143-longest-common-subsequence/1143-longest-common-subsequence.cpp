class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();
        int c[m+1][n+1];
        for(int i=0;i<=m;i++){
            c[i][0] = 0;
        }
        for(int j=0;j<=n;j++){
            c[0][j] = 0;
        }
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(text1[i-1]!=text2[j-1])
                    c[i][j] = max(c[i][j-1],c[i-1][j]);
                if(text1[i-1]==text2[j-1])
                    c[i][j] = c[i-1][j-1] + 1;
            }
        }
        return c[m][n];
    }
};