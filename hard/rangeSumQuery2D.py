"""
Given a 2D matrix matrix, handle multiple queries of the following type:
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
"""

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.matrix = []
            return

        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        # Build 2D prefix sum
        self.prefix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for i in range(self.rows):
            for j in range(self.cols):
                self.prefix[i + 1][j + 1] = (
                    self.prefix[i + 1][j]
                    + self.prefix[i][j + 1]
                    - self.prefix[i][j]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            - self.prefix[row1][col2 + 1]
            + self.prefix[row1][col1]
        )


# Test cases
if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(2, 1, 4, 3))  # Output: 8
    print(obj.sumRegion(1, 1, 2, 2))  # Output: 11
