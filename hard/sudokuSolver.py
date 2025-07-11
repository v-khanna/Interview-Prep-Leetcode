"""
Sudoku Solver (Hard)
https://leetcode.com/problems/sudoku-solver/

Problem: Write a program to solve a Sudoku puzzle by filling the empty cells.

Example:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

Approach: Backtracking with constraint propagation
Time Complexity: O(9^(n^2))
Space Complexity: O(n^2)
"""


class Solution:
    def solveSudoku(self, board):
        """
        Solve Sudoku using backtracking
        """

        def isValid(row, col, num):
            # Check row
            for j in range(9):
                if board[row][j] == str(num):
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == str(num):
                    return False

            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == str(num):
                        return False

            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if isValid(i, j, num):
                                board[i][j] = str(num)
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        solve()

    def solveSudokuOptimized(self, board):
        """
        Optimized version with better constraint checking
        """

        def findEmpty():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        return i, j
            return None

        def isValid(row, col, num):
            # Check row and column
            for i in range(9):
                if board[row][i] == str(num) or board[i][col] == str(num):
                    return False

            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == str(num):
                        return False

            return True

        def solve():
            empty = findEmpty()
            if not empty:
                return True

            row, col = empty
            for num in range(1, 10):
                if isValid(row, col, num):
                    board[row][col] = str(num)
                    if solve():
                        return True
                    board[row][col] = "."

            return False

        solve()

    def solveSudokuBitwise(self, board):
        """
        Bitwise approach for better performance
        """

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        # Get available numbers for this cell
                        available = getAvailableNumbers(i, j)
                        for num in range(1, 10):
                            if available & (1 << (num - 1)):
                                board[i][j] = str(num)
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True

        def getAvailableNumbers(row, col):
            available = 0b111111111  # All 9 bits set

            # Check row and column
            for i in range(9):
                if board[row][i] != ".":
                    available &= ~(1 << (int(board[row][i]) - 1))
                if board[i][col] != ".":
                    available &= ~(1 << (int(board[i][col]) - 1))

            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] != ".":
                        available &= ~(1 << (int(board[i][j]) - 1))

            return available

        solve()

    def solveSudokuConstraintPropagation(self, board):
        """
        Constraint propagation approach
        """

        def getCandidates(row, col):
            candidates = set(range(1, 10))

            # Remove numbers from row
            for j in range(9):
                if board[row][j] != ".":
                    candidates.discard(int(board[row][j]))

            # Remove numbers from column
            for i in range(9):
                if board[i][col] != ".":
                    candidates.discard(int(board[i][col]))

            # Remove numbers from 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] != ".":
                        candidates.discard(int(board[i][j]))

            return candidates

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        candidates = getCandidates(i, j)
                        for num in candidates:
                            board[i][j] = str(num)
                            if solve():
                                return True
                            board[i][j] = "."
                        return False
            return True

        solve()


def test_sudoku_solver():
    """Test cases for Sudoku Solver"""
    solution = Solution()

    # Test case 1: Standard Sudoku puzzle
    board1 = [
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

    # Test all methods
    methods = [
        solution.solveSudoku,
        solution.solveSudokuOptimized,
        solution.solveSudokuBitwise,
        solution.solveSudokuConstraintPropagation,
    ]

    for method in methods:
        # Create a copy of the board for each test
        test_board = [row[:] for row in board1]
        method(test_board)

        # Verify the solution is valid
        assert isValidSudoku(test_board)

    print("All test cases passed!")


def isValidSudoku(board):
    """Helper function to validate Sudoku solution"""
    # Check rows
    for row in board:
        if len(set(row)) != 9 or "." in row:
            return False

    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if len(set(column)) != 9:
            return False

    # Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    box.append(board[i][j])
            if len(set(box)) != 9:
                return False

    return True


if __name__ == "__main__":
    test_sudoku_solver()
