class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        i = j = 0
        
        right = True
        left = False
        down = False
        up = False
        
        res = []
        cnt = 0
        
        while cnt < m*n:
            
            ##STOP RIGHT GO DOWN
            if right and (j == n-1):
                right = False
                down = True
            elif right and matrix[i][j+1] == None:
                right = False
                down = True
                
            ##STOP DOWN GO LEFT    
            elif down and (i == m-1):
                down = False
                left = True
            elif down and matrix[i+1][j] == None:
                down = False
                left = True
                
            ##STOP LEFT GO UP    
            elif left and (j == 0):
                left = False
                up = True
            elif left and matrix[i][j-1] == None:
                left = False
                up = True
                
            #STOP UP GO RIGHT    
            elif up and (i == 0):
                up = False
                right = True
            elif up and matrix[i-1][j] == None:
                up = False
                right = True    
            
            #store the result
            res.append(matrix[i][j])
            cnt += 1
            
            #Block the place
            matrix[i][j] = None
            
            #NEXT MOVES
            if right: j += 1
            elif left: j -= 1
            elif down : i += 1
            elif up: i -= 1
            
        return res