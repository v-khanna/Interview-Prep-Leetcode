"""
Find Median from Data Stream (Hard)
https://leetcode.com/problems/find-median-from-data-stream/

Problem: The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

Example:
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output: [null, null, null, 1.5, null, 2.0]

Approach: Two heaps (max heap + min heap)
Time Complexity: O(log n) for addNum, O(1) for findMedian
Space Complexity: O(n)
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_heap = []  # Left half (max heap)
        self.min_heap = []  # Right half (min heap)

    def addNum(self, num):
        """
        Add a number into the data structure.
        """
        # Add to max heap first
        heapq.heappush(self.max_heap, -num)

        # Balance the heaps
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            # Move largest from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Ensure size balance
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self):
        """
        Returns the median of current data stream.
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


class MedianFinderOptimized:
    def __init__(self):
        """
        Optimized version with better balance strategy
        """
        self.small = []  # Max heap for smaller half
        self.large = []  # Min heap for larger half

    def addNum(self, num):
        """
        Add a number into the data structure.
        """
        # Always add to small heap first
        heapq.heappush(self.small, -num)

        # Move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance sizes
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Returns the median of current data stream.
        """
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


class MedianFinderWithCount:
    def __init__(self):
        """
        Version that tracks count for debugging
        """
        self.max_heap = []
        self.min_heap = []
        self.count = 0

    def addNum(self, num):
        """
        Add a number into the data structure.
        """
        self.count += 1

        # Add to appropriate heap based on count
        if self.count % 2 == 1:
            # Odd count, add to max_heap
            if self.min_heap and num > self.min_heap[0]:
                # Move smallest from min_heap to max_heap
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -val)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            # Even count, add to min_heap
            if self.max_heap and num < -self.max_heap[0]:
                # Move largest from max_heap to min_heap
                val = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val)
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

    def findMedian(self):
        """
        Returns the median of current data stream.
        """
        if self.count % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


def test_median_finder():
    """Test cases for Find Median from Data Stream"""

    # Test case 1: Basic operations
    medianFinder1 = MedianFinder()
    medianFinder1.addNum(1)
    medianFinder1.addNum(2)
    assert medianFinder1.findMedian() == 1.5
    medianFinder1.addNum(3)
    assert medianFinder1.findMedian() == 2.0

    # Test optimized version
    medianFinder2 = MedianFinderOptimized()
    medianFinder2.addNum(1)
    medianFinder2.addNum(2)
    assert medianFinder2.findMedian() == 1.5
    medianFinder2.addNum(3)
    assert medianFinder2.findMedian() == 2.0

    # Test count version
    medianFinder3 = MedianFinderWithCount()
    medianFinder3.addNum(1)
    medianFinder3.addNum(2)
    assert medianFinder3.findMedian() == 1.5
    medianFinder3.addNum(3)
    assert medianFinder3.findMedian() == 2.0

    # Test case 2: Single number
    medianFinder4 = MedianFinder()
    medianFinder4.addNum(5)
    assert medianFinder4.findMedian() == 5.0

    # Test case 3: Even number of elements
    medianFinder5 = MedianFinder()
    medianFinder5.addNum(1)
    medianFinder5.addNum(2)
    medianFinder5.addNum(3)
    medianFinder5.addNum(4)
    assert medianFinder5.findMedian() == 2.5

    # Test case 4: Negative numbers
    medianFinder6 = MedianFinder()
    medianFinder6.addNum(-1)
    medianFinder6.addNum(-2)
    assert medianFinder6.findMedian() == -1.5

    # Test case 5: Large numbers
    medianFinder7 = MedianFinder()
    medianFinder7.addNum(1000)
    medianFinder7.addNum(2000)
    medianFinder7.addNum(3000)
    assert medianFinder7.findMedian() == 2000.0

    print("All test cases passed!")


if __name__ == "__main__":
    test_median_finder()
