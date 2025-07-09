"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    )  # Output: [1,1,4,2,1,1,0,0]
    print(solution.dailyTemperatures([30, 40, 50, 60]))  # Output: [1,1,1,0]
