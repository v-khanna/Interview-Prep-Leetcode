"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False

            # Mark as visited
            temp = board[i][j]
            board[i][j] = "#"

            # Check all directions
            result = (
                dfs(i + 1, j, index + 1)
                or dfs(i - 1, j, index + 1)
                or dfs(i, j + 1, index + 1)
                or dfs(i, j - 1, index + 1)
            )

            # Restore
            board[i][j] = temp
            return result

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    print(solution.exist(board, "ABCCED"))  # True
    print(solution.exist(board, "SEE"))  # True
    print(solution.exist(board, "ABCB"))  # False
