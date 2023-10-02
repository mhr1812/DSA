class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False

        A_groups = colors.split("B")
        B_groups = colors.split("A")

        Alice_moves = 0
        Bob_moves = 0

        for A_group, B_group in zip(A_groups, B_groups):
            if len(A_group) >= 3:
                move = len(A_group) - 3 + 1
                Alice_moves += move
            if len(B_group) >= 3:
                move = len(B_group) - 3 + 1
                Bob_moves += move

        return Alice_moves > Bob_moves