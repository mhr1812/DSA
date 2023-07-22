NEXT_HOP_PROB = 1 / 8

class Solution:
    def knightProbability(self, size, moves, r, c):
        # use a dict to represent the board because the distribution is likely sparse
        probs = {(r, c): 1}
        for i in range(moves):
            new_probs = {}
            for coord, prob in probs.items():
                for new_coord in self._next_position_on_board(coord, size):
                    if new_coord not in new_probs:
                        new_probs[new_coord] = 0
                    new_probs[new_coord] += NEXT_HOP_PROB * prob
            probs = new_probs
        return sum(probs.values())
    
    def _next_position_on_board(self, coord, size):
        result = []
        for delta in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)):
            x, y = coord[0] + delta[0], coord[1] + delta[1]
            if 0 <= x < size and 0 <= y < size:
                result.append((x, y))
        return result