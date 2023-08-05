class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m,n = len(board),len(board[0])
        
        def dfs(i,j,word):
            if not word:
                return True 
            if i<0 or i>=m or j<0 or j>=n or word[0]!=board[i][j]:
                return False
            t = board[i][j]
            board[i][j] = 'v'
            ans = dfs(i+1,j,word[1:]) or dfs(i-1,j,word[1:]) or dfs(i,j+1,word[1:]) or dfs(i,j-1,word[1:])
            board[i][j] = t
            return ans
            
        for i in range(m):
            for j in range(n):
                if dfs(i,j,word):
                    return True 
        return False