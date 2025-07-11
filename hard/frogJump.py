"""
Frog Jump (Hard)
https://leetcode.com/problems/frog-jump/

Problem: A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Example:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true

Approach: Dynamic Programming with memoization
Time Complexity: O(n²)
Space Complexity: O(n²)
"""


class Solution:
    def canCross(self, stones):
        """
        Check if frog can cross the river using dynamic programming
        """
        if not stones or len(stones) < 2:
            return False

        # Create a set for O(1) lookup
        stone_set = set(stones)

        # dp[i][j] = can reach stone i with jump size j
        dp = {}

        def can_reach(position, jump_size):
            # Base case: reached the last stone
            if position == stones[-1]:
                return True

            # Check if this state has been computed
            if (position, jump_size) in dp:
                return dp[(position, jump_size)]

            # Try different jump sizes
            for next_jump in [jump_size - 1, jump_size, jump_size + 1]:
                if next_jump > 0:  # Jump size must be positive
                    next_position = position + next_jump
                    if next_position in stone_set:
                        if can_reach(next_position, next_jump):
                            dp[(position, jump_size)] = True
                            return True

            dp[(position, jump_size)] = False
            return False

        # Start from first stone with jump size 1
        return can_reach(stones[0], 0)

    def canCrossBFS(self, stones):
        """
        BFS approach with queue
        """
        if not stones or len(stones) < 2:
            return False

        stone_set = set(stones)
        visited = set()
        queue = [(0, 0)]  # (position, jump_size)

        while queue:
            position, jump_size = queue.pop(0)

            if position == stones[-1]:
                return True

            # Try different jump sizes
            for next_jump in [jump_size - 1, jump_size, jump_size + 1]:
                if next_jump > 0:
                    next_position = position + next_jump
                    if (
                        next_position in stone_set
                        and (next_position, next_jump) not in visited
                    ):
                        visited.add((next_position, next_jump))
                        queue.append((next_position, next_jump))

        return False

    def canCrossOptimized(self, stones):
        """
        Optimized version with early termination
        """
        if not stones or len(stones) < 2:
            return False

        n = len(stones)
        stone_set = set(stones)

        # dp[i][j] = can reach stone i with jump size j
        dp = {}

        def can_reach(position, jump_size):
            if position == stones[-1]:
                return True

            if (position, jump_size) in dp:
                return dp[(position, jump_size)]

            # Early termination: if we can't reach the end with current jump
            max_reachable = position + jump_size * (n - 1)
            if max_reachable < stones[-1]:
                dp[(position, jump_size)] = False
                return False

            for next_jump in [jump_size - 1, jump_size, jump_size + 1]:
                if next_jump > 0:
                    next_position = position + next_jump
                    if next_position in stone_set:
                        if can_reach(next_position, next_jump):
                            dp[(position, jump_size)] = True
                            return True

            dp[(position, jump_size)] = False
            return False

        return can_reach(stones[0], 0)

    def canCrossIterative(self, stones):
        """
        Iterative DP approach
        """
        if not stones or len(stones) < 2:
            return False

        n = len(stones)
        stone_set = set(stones)

        # dp[i] = set of jump sizes that can reach stone i
        dp = [set() for _ in range(n)]
        dp[0].add(0)  # Can reach first stone with jump size 0

        for i in range(n):
            for jump_size in dp[i]:
                # Try next jumps
                for next_jump in [jump_size - 1, jump_size, jump_size + 1]:
                    if next_jump > 0:
                        next_position = stones[i] + next_jump
                        if next_position in stone_set:
                            # Find index of next_position
                            for j in range(i + 1, n):
                                if stones[j] == next_position:
                                    dp[j].add(next_jump)
                                    break

        return len(dp[n - 1]) > 0


def test_frog_jump():
    """Test cases for Frog Jump"""
    solution = Solution()

    # Test case 1: Basic case
    stones1 = [0, 1, 3, 5, 6, 8, 12, 17]
    assert solution.canCross(stones1) == True
    assert solution.canCrossBFS(stones1) == True
    assert solution.canCrossOptimized(stones1) == True
    assert solution.canCrossIterative(stones1) == True

    # Test case 2: Cannot cross
    stones2 = [0, 1, 2, 3, 4, 8, 9, 11]
    assert solution.canCross(stones2) == False
    assert solution.canCrossBFS(stones2) == False
    assert solution.canCrossOptimized(stones2) == False
    assert solution.canCrossIterative(stones2) == False

    # Test case 3: Single stone
    stones3 = [0]
    assert solution.canCross(stones3) == False
    assert solution.canCrossBFS(stones3) == False
    assert solution.canCrossOptimized(stones3) == False
    assert solution.canCrossIterative(stones3) == False

    # Test case 4: Two stones
    stones4 = [0, 1]
    assert solution.canCross(stones4) == True
    assert solution.canCrossBFS(stones4) == True
    assert solution.canCrossOptimized(stones4) == True
    assert solution.canCrossIterative(stones4) == True

    # Test case 5: Three stones
    stones5 = [0, 1, 3]
    assert solution.canCross(stones5) == True
    assert solution.canCrossBFS(stones5) == True
    assert solution.canCrossOptimized(stones5) == True
    assert solution.canCrossIterative(stones5) == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_frog_jump()
