"""
Candy (Hard)
https://leetcode.com/problems/candy/

Problem: There are n children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

Example:
Input: [1,0,2]
Output: 5 (2,1,2 candies respectively)

Approach: Two-pass greedy algorithm
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def candy(self, ratings):
        """
        Find minimum candies using two-pass greedy approach
        """
        if not ratings:
            return 0

        n = len(ratings)
        candies = [1] * n

        # First pass: left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Second pass: right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

    def candyOnePass(self, ratings):
        """
        Alternative approach using one pass with peak detection
        """
        if not ratings:
            return 0

        n = len(ratings)
        candies = [1] * n

        # Handle increasing sequences
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Handle decreasing sequences and peaks
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

    def candyOptimized(self, ratings):
        """
        Optimized approach with O(1) space for understanding
        """
        if not ratings:
            return 0

        n = len(ratings)
        total = 1  # First child gets 1 candy
        up = 1  # Length of current increasing sequence
        down = 0  # Length of current decreasing sequence
        peak = 1  # Peak of current mountain

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                # Going up
                up += 1
                down = 0
                peak = up
                total += up
            elif ratings[i] < ratings[i - 1]:
                # Going down
                down += 1
                up = 1
                total += down
                if peak <= down:
                    total += 1  # Need to increase peak
            else:
                # Equal ratings
                up = 1
                down = 0
                peak = 1
                total += 1

        return total

    def candyWithConstraints(self, ratings, min_candy=1):
        """
        Extension: with minimum candy constraint
        """
        if not ratings:
            return 0

        n = len(ratings)
        candies = [min_candy] * n

        # First pass: left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Second pass: right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

    def candyWithEqualHandling(self, ratings):
        """
        Alternative approach that handles equal ratings differently
        """
        if not ratings:
            return 0

        n = len(ratings)
        candies = [1] * n

        # First pass: left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            elif ratings[i] == ratings[i - 1]:
                candies[i] = (
                    1  # Can be 1 since equal ratings don't require more candies
                )

        # Second pass: right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            elif ratings[i] == ratings[i + 1]:
                candies[i] = max(candies[i], 1)  # At least 1 candy

        return sum(candies)


def test_candy():
    """Test cases for Candy"""
    solution = Solution()

    # Test case 1: Basic case
    ratings1 = [1, 0, 2]
    assert solution.candy(ratings1) == 5
    assert solution.candyOnePass(ratings1) == 5
    assert solution.candyOptimized(ratings1) == 5
    assert solution.candyWithConstraints(ratings1) == 5
    assert solution.candyWithEqualHandling(ratings1) == 5

    # Test case 2: All same ratings
    ratings2 = [1, 2, 2]
    assert solution.candy(ratings2) == 4
    assert solution.candyOnePass(ratings2) == 4
    assert solution.candyOptimized(ratings2) == 4
    assert solution.candyWithConstraints(ratings2) == 4
    assert solution.candyWithEqualHandling(ratings2) == 4

    # Test case 3: Strictly increasing
    ratings3 = [1, 2, 3, 4, 5]
    assert solution.candy(ratings3) == 15
    assert solution.candyOnePass(ratings3) == 15
    assert solution.candyOptimized(ratings3) == 15
    assert solution.candyWithConstraints(ratings3) == 15
    assert solution.candyWithEqualHandling(ratings3) == 15

    # Test case 4: Strictly decreasing
    ratings4 = [5, 4, 3, 2, 1]
    assert solution.candy(ratings4) == 15
    assert solution.candyOnePass(ratings4) == 15
    assert solution.candyOptimized(ratings4) == 15
    assert solution.candyWithConstraints(ratings4) == 15
    assert solution.candyWithEqualHandling(ratings4) == 15

    # Test case 5: Single rating
    ratings5 = [1]
    assert solution.candy(ratings5) == 1
    assert solution.candyOnePass(ratings5) == 1
    assert solution.candyOptimized(ratings5) == 1
    assert solution.candyWithConstraints(ratings5) == 1
    assert solution.candyWithEqualHandling(ratings5) == 1

    # Test case 6: Empty array
    ratings6 = []
    assert solution.candy(ratings6) == 0
    assert solution.candyOnePass(ratings6) == 0
    assert solution.candyOptimized(ratings6) == 0
    assert solution.candyWithConstraints(ratings6) == 0
    assert solution.candyWithEqualHandling(ratings6) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_candy()
