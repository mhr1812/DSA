class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_counter = 0
        b_counter = 0
        last_len = len(colors)
        all_colors = 'AB'
        for color in all_colors:
            while color * 3 in colors:
                colors = colors.replace(color * 3, color * 2)
                if color == 'A':
                    a_counter += (last_len - len(colors))
                    last_len = len(colors)
                else:
                    b_counter += (last_len - len(colors))
                    last_len = len(colors)
        
        return a_counter > b_counter