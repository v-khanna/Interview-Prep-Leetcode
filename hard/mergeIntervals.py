"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        current = intervals[0]

        for interval in intervals[1:]:
            # If current interval overlaps with next interval
            if current[1] >= interval[0]:
                current[1] = max(current[1], interval[1])
            else:
                merged.append(current)
                current = interval

        merged.append(current)
        return merged


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
    print(solution.merge([[1, 4], [4, 5]]))  # [[1,5]]
    print(solution.merge([[1, 4], [2, 3]]))  # [[1,4]]
