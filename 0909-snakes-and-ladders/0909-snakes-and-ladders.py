# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         board.reverse()
#         for i in range(1,len(board),2):
#             board[i].reverse()
        
#         arr = [None] + list(chain(*board))
        
#         n, queue, seen, c = len(arr)-1, deque([1]), {1}, 0
        
#         while queue:
#             l = len(queue)
            
#             for _ in range(l):
#                 curr = queue.popleft()
                
#                 if curr==n:
#                     return c
                
#                 for i in range(curr+1,min(curr+7,curr+1)):
#                     nxt = max(arr[i],i)
                   
#                     if nxt in seen:
#                         continue
#                     seen.add(nxt)
#                     queue.append(nxt)
#             c+=1
        
#         return -1 
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        board.reverse()                                     #  <–– convert the board to 1D list
        for i in range(1,len(board),2): board[i].reverse()
        arr = [None]+list(chain(*board))                    #  <–– add an initial element (None) 
                                                            #      to make indexing simpler
                                                            
        n, queue, seen, ct = len(arr)-1, deque([1]), {1}, 0               

        while queue:                                        #  <–– BFS search for arr[n]
            lenQ = len(queue)

            for _ in range(lenQ):                           #  <–– one level of BFS

                cur = queue.popleft()
                if cur == n: return ct

                for i in range(cur+1, min(cur+7,n+1)):      #  <–– oiterate through the possible next moves
                    nxt = arr[i] if arr[i]+1 else i         #  <–– determine whether snake or ladder

                    if nxt in seen: continue                #  <–– avoid revisiting positions        
                    seen.add(nxt)
                    queue.append(nxt)                       #  <–– build queue for next level
                    
            ct += 1                    
        
        return -1
            