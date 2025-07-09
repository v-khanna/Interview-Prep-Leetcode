"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise) in-place.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()


# Test cases
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    print(matrix)  # Output: [[7,4,1],[8,5,2],[9,6,3]]
