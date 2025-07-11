"""
Game of Life (Hard)
https://leetcode.com/problems/game-of-life/

Problem: According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Example:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Approach: In-place modification with encoding
Time Complexity: O(mn)
Space Complexity: O(1)
"""


class Solution:
    def gameOfLife(self, board):
        """
        Update the board in-place using encoding
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        # Directions: 8 neighbors
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # First pass: encode the next state
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                # Count live neighbors
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        # Check if neighbor was live in previous state
                        if board[ni][nj] in [1, 2]:  # 2 means live->dead
                            live_neighbors += 1

                # Apply rules
                if board[i][j] == 1:  # Currently live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # live->dead
                else:  # Currently dead
                    if live_neighbors == 3:
                        board[i][j] = 3  # dead->live

        # Second pass: decode the next state
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

    def gameOfLifeWithCopy(self, board):
        """
        Alternative approach using a copy of the board
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        # Create a copy of the board
        board_copy = [row[:] for row in board]

        # Directions: 8 neighbors
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                # Count live neighbors from the copy
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board_copy[ni][nj] == 1:
                        live_neighbors += 1

                # Apply rules
                if board_copy[i][j] == 1:  # Currently live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 0
                else:  # Currently dead
                    if live_neighbors == 3:
                        board[i][j] = 1

    def gameOfLifeOptimized(self, board):
        """
        Optimized version with better encoding
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        # Directions: 8 neighbors
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # First pass: encode next state
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        # Check if neighbor was live (1 or 2)
                        if board[ni][nj] & 1:
                            live_neighbors += 1

                # Apply rules and encode
                if board[i][j] == 1:  # Currently live
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[i][j] = 3  # 11 in binary: live->live
                else:  # Currently dead
                    if live_neighbors == 3:
                        board[i][j] = 2  # 10 in binary: dead->live

        # Second pass: decode
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1  # Shift right to get next state

    def gameOfLifeWithBoundary(self, board):
        """
        Version that handles boundary conditions explicitly
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        # Create a padded board for easier neighbor counting
        padded = [[0] * (n + 2) for _ in range(m + 2)]

        # Copy original board to padded board
        for i in range(m):
            for j in range(n):
                padded[i + 1][j + 1] = board[i][j]

        # Update original board based on padded board
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                # Count live neighbors in padded board
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        if padded[i + 1 + di][j + 1 + dj] == 1:
                            live_neighbors += 1

                # Apply rules
                if padded[i + 1][j + 1] == 1:  # Currently live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 0
                else:  # Currently dead
                    if live_neighbors == 3:
                        board[i][j] = 1


def test_game_of_life():
    """Test cases for Game of Life"""
    solution = Solution()

    # Test case 1: Basic case
    board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    expected1 = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    # Test in-place version
    board1_copy = [row[:] for row in board1]
    solution.gameOfLife(board1_copy)
    assert board1_copy == expected1

    # Test copy version
    board1_copy2 = [row[:] for row in board1]
    solution.gameOfLifeWithCopy(board1_copy2)
    assert board1_copy2 == expected1

    # Test optimized version
    board1_copy3 = [row[:] for row in board1]
    solution.gameOfLifeOptimized(board1_copy3)
    assert board1_copy3 == expected1

    # Test boundary version
    board1_copy4 = [row[:] for row in board1]
    solution.gameOfLifeWithBoundary(board1_copy4)
    assert board1_copy4 == expected1

    # Test case 2: All dead
    board2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    expected2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    board2_copy = [row[:] for row in board2]
    solution.gameOfLife(board2_copy)
    assert board2_copy == expected2

    # Test case 3: Single live cell
    board3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    board3_copy = [row[:] for row in board3]
    solution.gameOfLife(board3_copy)
    assert board3_copy == expected3

    # Test case 4: Blinker pattern
    board4 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    expected4 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

    board4_copy = [row[:] for row in board4]
    solution.gameOfLife(board4_copy)
    assert board4_copy == expected4

    print("All test cases passed!")


if __name__ == "__main__":
    test_game_of_life()
