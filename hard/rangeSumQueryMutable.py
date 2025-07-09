"""
Given an integer array nums, handle multiple queries of the following types:
1. Update the value of an element in nums.
2. Calculate the sum of the elements of nums between indices left and right inclusive.
"""

from typing import List


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return

        mid = (start + end) // 2
        self.build(nums, 2 * node + 1, start, mid)
        self.build(nums, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index, val):
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, node, start, end, index, val):
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        if index <= mid:
            self._update(2 * node + 1, start, mid, index, val)
        else:
            self._update(2 * node + 2, mid + 1, end, index, val)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node, start, end, left, right):
        if right < start or left > end:
            return 0
        if left <= start and right >= end:
            return self.tree[node]

        mid = (start + end) // 2
        return self._query(2 * node + 1, start, mid, left, right) + self._query(
            2 * node + 2, mid + 1, end, left, right
        )


class NumArray:
    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.query(left, right)


# Test cases
if __name__ == "__main__":
    nums = [1, 3, 5]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))  # Output: 9
    obj.update(1, 2)
    print(obj.sumRange(0, 2))  # Output: 8
