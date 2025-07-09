"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Return the number of distinct solutions to the n-queens puzzle.
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diags1, diags2):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in cols or (row - col) in diags1 or (row + col) in diags2:
                    continue
                count += backtrack(
                    row + 1, cols | {col}, diags1 | {row - col}, diags2 | {row + col}
                )
            return count

        return backtrack(0, set(), set(), set())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.totalNQueens(4))  # Output: 2
    print(solution.totalNQueens(8))  # Output: 92
