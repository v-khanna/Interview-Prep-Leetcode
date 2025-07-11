"""
Largest Rectangle in Histogram (Hard)
https://leetcode.com/problems/largest-rectangle-in-histogram/

Problem: Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10

Approach: Monotonic stack
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def largestRectangleArea(self, heights):
        """
        Find largest rectangle area using monotonic stack
        """
        if not heights:
            return 0

        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            # Pop bars that are taller than current bar
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        # Process remaining bars in stack
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area

    def largestRectangleAreaOptimized(self, heights):
        """
        Optimized version with sentinel values
        """
        if not heights:
            return 0

        # Add sentinel values
        heights = [0] + heights + [0]
        stack = [0]  # Initialize with sentinel index
        max_area = 0

        for i in range(1, len(heights)):
            # Pop bars that are taller than current bar
            while heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area

    def largestRectangleAreaDP(self, heights):
        """
        Dynamic programming approach
        """
        if not heights:
            return 0

        n = len(heights)
        left = [0] * n  # Left boundary for each bar
        right = [n] * n  # Right boundary for each bar

        # Find left boundaries
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        # Find right boundaries
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate areas
        max_area = 0
        for i in range(n):
            area = heights[i] * (right[i] - left[i])
            max_area = max(max_area, area)

        return max_area


def test_largest_rectangle_in_histogram():
    """Test cases for Largest Rectangle in Histogram"""
    solution = Solution()

    # Test case 1: Basic case
    heights1 = [2, 1, 5, 6, 2, 3]
    assert solution.largestRectangleArea(heights1) == 10
    assert solution.largestRectangleAreaOptimized(heights1) == 10
    assert solution.largestRectangleAreaDP(heights1) == 10

    # Test case 2: Single bar
    heights2 = [1]
    assert solution.largestRectangleArea(heights2) == 1
    assert solution.largestRectangleAreaOptimized(heights2) == 1
    assert solution.largestRectangleAreaDP(heights2) == 1

    # Test case 3: All same height
    heights3 = [2, 2, 2, 2]
    assert solution.largestRectangleArea(heights3) == 8
    assert solution.largestRectangleAreaOptimized(heights3) == 8
    assert solution.largestRectangleAreaDP(heights3) == 8

    # Test case 4: Increasing heights
    heights4 = [1, 2, 3, 4, 5]
    assert solution.largestRectangleArea(heights4) == 9
    assert solution.largestRectangleAreaOptimized(heights4) == 9
    assert solution.largestRectangleAreaDP(heights4) == 9

    # Test case 5: Empty array
    heights5 = []
    assert solution.largestRectangleArea(heights5) == 0
    assert solution.largestRectangleAreaOptimized(heights5) == 0
    assert solution.largestRectangleAreaDP(heights5) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_largest_rectangle_in_histogram()
