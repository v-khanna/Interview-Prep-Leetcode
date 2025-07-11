"""
Maximal Rectangle (Hard)
https://leetcode.com/problems/maximal-rectangle/

Problem: Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6

Approach: Dynamic Programming with histogram approach
Time Complexity: O(mn)
Space Complexity: O(n)
"""


class Solution:
    def maximalRectangle(self, matrix):
        """
        Find maximal rectangle using histogram approach
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            # Update heights for current row
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Calculate largest rectangle in histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        """
        Helper function to find largest rectangle in histogram
        """
        if not heights:
            return 0

        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area

    def maximalRectangleDP(self, matrix):
        """
        Dynamic programming approach
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [0] * n  # Left boundary
        right = [n] * n  # Right boundary
        height = [0] * n  # Height of current rectangle
        max_area = 0

        for i in range(m):
            # Update height
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            # Update left boundary
            curr_left = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curr_left)
                else:
                    left[j] = 0
                    curr_left = j + 1

            # Update right boundary
            curr_right = n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j] = n
                    curr_right = j

            # Calculate area
            for j in range(n):
                area = height[j] * (right[j] - left[j])
                max_area = max(max_area, area)

        return max_area

    def maximalRectangleOptimized(self, matrix):
        """
        Optimized version with better space usage
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)  # Add sentinel
        max_area = 0

        for i in range(m):
            # Update heights
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Calculate area using stack
            stack = [-1]
            for j in range(n + 1):
                while heights[stack[-1]] > heights[j]:
                    height = heights[stack.pop()]
                    width = j - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(j)

        return max_area


def test_maximal_rectangle():
    """Test cases for Maximal Rectangle"""
    solution = Solution()

    # Test case 1: Basic case
    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert solution.maximalRectangle(matrix1) == 6
    assert solution.maximalRectangleDP(matrix1) == 6
    assert solution.maximalRectangleOptimized(matrix1) == 6

    # Test case 2: Single row
    matrix2 = [["1", "1", "1", "1"]]
    assert solution.maximalRectangle(matrix2) == 4
    assert solution.maximalRectangleDP(matrix2) == 4
    assert solution.maximalRectangleOptimized(matrix2) == 4

    # Test case 3: Single column
    matrix3 = [["1"], ["1"], ["1"]]
    assert solution.maximalRectangle(matrix3) == 3
    assert solution.maximalRectangleDP(matrix3) == 3
    assert solution.maximalRectangleOptimized(matrix3) == 3

    # Test case 4: All zeros
    matrix4 = [["0", "0"], ["0", "0"]]
    assert solution.maximalRectangle(matrix4) == 0
    assert solution.maximalRectangleDP(matrix4) == 0
    assert solution.maximalRectangleOptimized(matrix4) == 0

    # Test case 5: All ones
    matrix5 = [["1", "1"], ["1", "1"]]
    assert solution.maximalRectangle(matrix5) == 4
    assert solution.maximalRectangleDP(matrix5) == 4
    assert solution.maximalRectangleOptimized(matrix5) == 4

    # Test case 6: Empty matrix
    matrix6 = []
    assert solution.maximalRectangle(matrix6) == 0
    assert solution.maximalRectangleDP(matrix6) == 0
    assert solution.maximalRectangleOptimized(matrix6) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_maximal_rectangle()
