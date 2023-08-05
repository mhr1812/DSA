POSITION_MODIFIERS = ((0, 1), (1, 0), (-1, 0), (0, -1))

class Solution:
    def _exist(self, board, word, word_pos, i, j, visited) -> bool:
        if word_pos == len(word):
            return True

        if (i, j) in visited:
            return False

        if i >= len(board) or i < 0:
            return False

        if j >= len(board[0]) or j < 0:
            return False

        if board[i][j] != word[word_pos]:
            return False

        visited.add(
            (i, j)
        )

        for mod_i, mod_j in POSITION_MODIFIERS:
            updated_i = i + mod_i
            updated_j = j + mod_j

            if self._exist(
                board, word, word_pos+1, updated_i, updated_j, visited
            ):
                return True

        visited.remove(
            (i, j)
        )

        return False

    def _exist_starting_from_cell(
        self, 
        board: List[List[str]], 
        word: str,
        i: int,
        j: int
    ) -> bool:
        return self._exist(
            board, word, word_pos=0, i=i, j=j, visited=set()
        )
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self._exist_starting_from_cell(board, word, i, j):
                    return True
        return False