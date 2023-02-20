class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        for i in range(1,len(board),2):
            board[i].reverse()
        
        arr = [None] + list(chain(*board))
        
        n, queue, seen, c = len(arr)-1, deque([1]), {1}, 0
        
        while queue:
            l = len(queue)
            
            for _ in range(l):
                curr = queue.popleft()
                
                if curr==n:
                    return c
                
                for i in range(curr+1,min(curr+7,n+1)):
                    if arr[i]==-1:
                        nxt = i
                    else:
                        nxt = arr[i]
                   
                    if nxt in seen:
                        continue
                    seen.add(nxt)
                    queue.append(nxt)
            c+=1
        
        return -1 
            