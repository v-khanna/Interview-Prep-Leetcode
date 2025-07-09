"""
Given a non-empty array of integers, return the k most frequent elements.
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [
            item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])
        ]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1,2]
    print(solution.topKFrequent([1], 1))  # Output: [1]
