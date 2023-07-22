class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        tNodes = 0
        cache = []
        for i in range(k):
            cache.append([[-1] * n for _ in range(n)])
        
        moves = [ (2,1),(2,-1),(-2,1),(-2,-1), (1,2),(1,-2),(-1,2),(-1,-2) ]

        def inRange(t):
            return t>=0 and t<n

        def dfs(curK, r, c):
            if curK==k:
                #nonlocal tNodes
                #tNodes += 1
                return 1

            #curK += 1
            tmp = 0

            for rMove, cMove in moves:
                rp = r + rMove
                cp = c + cMove

                if inRange(rp) and inRange(cp):

                    #see if result is already cached
                    if cache[curK][rp][cp]==-1:
                        z = dfs(curK+1, rp, cp)

                        #add z in cache
                        for x, y in [(rp, cp), (cp, rp)]:
                            cache[curK][x][y] = z

                            #vertical image
                            cache[curK][x][n-1-y] = z

                            #horizontal image
                            cache[curK][n-1-x][y] = z

                            #other diagonal image
                            cache[curK][n-1-y][n-1-x] = z

                    else:
                        z = cache[curK][rp][cp]

                    tmp += z

            return tmp

        tNodes = dfs(0, row, column)
        
        print(tNodes)
        res = tNodes * pow(0.125, k)
        return res