class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        sm1,sm2=0,0
        for i in range(n):
            f1,f2 = 0,0
            if i>=1:
                if player1[i-1]==10:
                    sm1+=2*player1[i]
                    f1 = 1
                    
                if player2[i-1]==10:
                    sm2+=2*player2[i]
                    f2 = 1
                
            if i>=2 and f1==0:
                if player1[i-2]==10:
                    sm1+=2*player1[i]
                    f1 = 1
            
            if i>=2 and f2==0:        
                if player2[i-2]==10:
                    sm2+=2*player2[i]
                    f2 = 1
                    
            if f1==0:
                sm1+=player1[i]
            if f2==0:
                sm2+=player2[i]
        if sm1>sm2:
            return 1
        elif sm1<sm2:
            return 2
        else:
            return 0
            
            