"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.isValidUnit(row):
                return False

        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isValidUnit(column):
                return False

        # Check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        box.append(board[row][col])
                if not self.isValidUnit(box):
                    return False

        return True

    def isValidUnit(self, unit):
        seen = set()
        for cell in unit:
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solution.isValidSudoku(board))  # Output: True
