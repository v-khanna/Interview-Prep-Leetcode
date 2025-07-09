"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        result = []
        dq = deque()

        for i in range(len(nums)):
            # Remove elements outside the window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Add maximum to result when window is full
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    )  # Output: [3,3,5,5,6,7]
    print(solution.maxSlidingWindow([1], 1))  # Output: [1]
