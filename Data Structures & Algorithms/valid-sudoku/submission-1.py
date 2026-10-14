from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_row = defaultdict(set)
        board_column = defaultdict(set)
        board_square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if (val in board_row[i] or
                        val in board_column[j] or
                        val in board_square[(i // 3, j // 3)]):
                        return False

                    board_row[i].add(val)
                    board_column[j].add(val)
                    board_square[(i // 3, j // 3)].add(val)
        
        return True
