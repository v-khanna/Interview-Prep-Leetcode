from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate width and height
            width = right - left
            h = min(height[left], height[right])

            # Calculate area
            area = width * h
            max_area = max(max_area, area)

            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = solution.maxArea(height1)
    print(f"Max area for {height1}: {result1}")  # Expected: 49

    # Test case 2
    height2 = [1, 1]
    result2 = solution.maxArea(height2)
    print(f"Max area for {height2}: {result2}")  # Expected: 1

    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    result3 = solution.maxArea(height3)
    print(f"Max area for {height3}: {result3}")  # Expected: 16
