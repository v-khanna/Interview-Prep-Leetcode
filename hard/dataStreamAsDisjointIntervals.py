"""
Data Stream as Disjoint Intervals (Hard)
https://leetcode.com/problems/data-stream-as-disjoint-intervals/

Problem: Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Example:
Input: ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output: [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Approach: TreeSet to maintain sorted intervals
Time Complexity: O(log n) for addNum, O(n) for getIntervals
Space Complexity: O(n)
"""

from bisect import bisect_left, bisect_right


class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []  # List of [start, end] intervals

    def addNum(self, value):
        """
        Add a number to the data stream.
        """
        # Find position to insert
        pos = bisect_left(self.intervals, [value, value])

        # Check if value already exists in an interval
        if pos > 0 and self.intervals[pos - 1][1] >= value:
            return  # Value already in an interval

        # Check if we can merge with previous interval
        merge_prev = pos > 0 and self.intervals[pos - 1][1] + 1 == value

        # Check if we can merge with next interval
        merge_next = pos < len(self.intervals) and self.intervals[pos][0] - 1 == value

        if merge_prev and merge_next:
            # Merge with both previous and next intervals
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            self.intervals.pop(pos)
        elif merge_prev:
            # Merge with previous interval
            self.intervals[pos - 1][1] = value
        elif merge_next:
            # Merge with next interval
            self.intervals[pos][0] = value
        else:
            # Insert new interval
            self.intervals.insert(pos, [value, value])

    def getIntervals(self):
        """
        Return a list of disjoint intervals.
        """
        return self.intervals


class SummaryRangesOptimized:
    def __init__(self):
        """
        Optimized version using set for O(1) lookup
        """
        self.nums = set()

    def addNum(self, value):
        """
        Add a number to the data stream.
        """
        self.nums.add(value)

    def getIntervals(self):
        """
        Return a list of disjoint intervals.
        """
        if not self.nums:
            return []

        intervals = []
        start = end = None

        for num in sorted(self.nums):
            if start is None:
                start = end = num
            elif num == end + 1:
                end = num
            else:
                intervals.append([start, end])
                start = end = num

        intervals.append([start, end])
        return intervals


class SummaryRangesTreeSet:
    def __init__(self):
        """
        TreeSet-like implementation using sorted list
        """
        self.nums = []

    def addNum(self, value):
        """
        Add a number to the data stream.
        """
        # Find insertion position
        pos = bisect_left(self.nums, value)

        # Check if value already exists
        if pos < len(self.nums) and self.nums[pos] == value:
            return

        # Insert value
        self.nums.insert(pos, value)

    def getIntervals(self):
        """
        Return a list of disjoint intervals.
        """
        if not self.nums:
            return []

        intervals = []
        start = end = self.nums[0]

        for i in range(1, len(self.nums)):
            if self.nums[i] == end + 1:
                end = self.nums[i]
            else:
                intervals.append([start, end])
                start = end = self.nums[i]

        intervals.append([start, end])
        return intervals


class SummaryRangesUnionFind:
    def __init__(self):
        """
        Union-Find based approach
        """
        self.parent = {}
        self.rank = {}
        self.min_val = {}
        self.max_val = {}

    def addNum(self, value):
        """
        Add a number to the data stream.
        """
        if value in self.parent:
            return

        # Initialize new element
        self.parent[value] = value
        self.rank[value] = 0
        self.min_val[value] = value
        self.max_val[value] = value

        # Union with neighbors
        if value - 1 in self.parent:
            self._union(value - 1, value)
        if value + 1 in self.parent:
            self._union(value, value + 1)

    def _find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self._find(self.parent[x])
        return self.parent[x]

    def _union(self, x, y):
        """Union by rank"""
        root_x = self._find(x)
        root_y = self._find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.min_val[root_x] = min(self.min_val[root_x], self.min_val[root_y])
        self.max_val[root_x] = max(self.max_val[root_x], self.max_val[root_y])

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

    def getIntervals(self):
        """
        Return a list of disjoint intervals.
        """
        intervals = []
        seen = set()

        for value in self.parent:
            root = self._find(value)
            if root not in seen:
                intervals.append([self.min_val[root], self.max_val[root]])
                seen.add(root)

        return sorted(intervals)


def test_summary_ranges():
    """Test cases for Data Stream as Disjoint Intervals"""

    # Test case 1: Basic operations
    summary1 = SummaryRanges()
    summary1.addNum(1)
    assert summary1.getIntervals() == [[1, 1]]
    summary1.addNum(3)
    assert summary1.getIntervals() == [[1, 1], [3, 3]]
    summary1.addNum(7)
    assert summary1.getIntervals() == [[1, 1], [3, 3], [7, 7]]
    summary1.addNum(2)
    assert summary1.getIntervals() == [[1, 3], [7, 7]]
    summary1.addNum(6)
    assert summary1.getIntervals() == [[1, 3], [6, 7]]

    # Test optimized version
    summary2 = SummaryRangesOptimized()
    summary2.addNum(1)
    assert summary2.getIntervals() == [[1, 1]]
    summary2.addNum(3)
    assert summary2.getIntervals() == [[1, 1], [3, 3]]

    # Test TreeSet version
    summary3 = SummaryRangesTreeSet()
    summary3.addNum(1)
    assert summary3.getIntervals() == [[1, 1]]
    summary3.addNum(3)
    assert summary3.getIntervals() == [[1, 1], [3, 3]]

    # Test Union-Find version
    summary4 = SummaryRangesUnionFind()
    summary4.addNum(1)
    assert summary4.getIntervals() == [[1, 1]]
    summary4.addNum(3)
    assert summary4.getIntervals() == [[1, 1], [3, 3]]

    # Test case 2: Consecutive numbers
    summary5 = SummaryRanges()
    summary5.addNum(1)
    summary5.addNum(2)
    summary5.addNum(3)
    assert summary5.getIntervals() == [[1, 3]]

    # Test case 3: Empty stream
    summary6 = SummaryRanges()
    assert summary6.getIntervals() == []

    # Test case 4: Duplicate numbers
    summary7 = SummaryRanges()
    summary7.addNum(1)
    summary7.addNum(1)  # Duplicate
    assert summary7.getIntervals() == [[1, 1]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_summary_ranges()
