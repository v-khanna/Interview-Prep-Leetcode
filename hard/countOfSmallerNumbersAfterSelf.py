"""
Count of Smaller Numbers After Self (Hard)
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Problem: You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:
Input: [5,2,6,1]
Output: [2,1,1,0]

Approach: Merge sort with counting inversions
Time Complexity: O(n log n)
Space Complexity: O(n)
"""


class Solution:
    def countSmaller(self, nums):
        """
        Count smaller numbers using merge sort approach
        """
        if not nums:
            return []

        n = len(nums)
        # Create array of (value, original_index) pairs
        indexed_nums = [(nums[i], i) for i in range(n)]
        result = [0] * n

        self._merge_sort(indexed_nums, 0, n - 1, result)
        return result

    def _merge_sort(self, nums, start, end, result):
        """Merge sort with counting smaller elements"""
        if start >= end:
            return

        mid = (start + end) // 2
        self._merge_sort(nums, start, mid, result)
        self._merge_sort(nums, mid + 1, end, result)
        self._merge(nums, start, mid, end, result)

    def _merge(self, nums, start, mid, end, result):
        """Merge two sorted arrays and count inversions"""
        left = nums[start : mid + 1]
        right = nums[mid + 1 : end + 1]

        i = j = 0
        k = start
        smaller_count = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                # Update count for left element
                result[left[i][1]] += smaller_count
                nums[k] = left[i]
                i += 1
            else:
                # Right element is smaller, increment count
                smaller_count += 1
                nums[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            result[left[i][1]] += smaller_count
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    def countSmallerBST(self, nums):
        """
        Alternative approach using Binary Search Tree
        """
        if not nums:
            return []

        class BSTNode:
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None
                self.count = 1  # Count of nodes in left subtree
                self.dup = 1  # Count of duplicates

        def insert(root, val, result, index, smaller_count):
            if not root:
                result[index] = smaller_count
                return BSTNode(val)

            if val == root.val:
                root.dup += 1
                result[index] = smaller_count + root.count
            elif val < root.val:
                root.count += 1
                root.left = insert(root.left, val, result, index, smaller_count)
            else:
                root.right = insert(
                    root.right,
                    val,
                    result,
                    index,
                    smaller_count + root.count + root.dup,
                )

            return root

        result = [0] * len(nums)
        root = None

        # Insert from right to left
        for i in range(len(nums) - 1, -1, -1):
            root = insert(root, nums[i], result, i, 0)

        return result

    def countSmallerBinaryIndexedTree(self, nums):
        """
        Alternative approach using Binary Indexed Tree (Fenwick Tree)
        """
        if not nums:
            return []

        # Coordinate compression
        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}

        class BIT:
            def __init__(self, n):
                self.tree = [0] * (n + 1)

            def update(self, index, val):
                while index < len(self.tree):
                    self.tree[index] += val
                    index += index & -index

            def query(self, index):
                total = 0
                while index > 0:
                    total += self.tree[index]
                    index -= index & -index
                return total

        bit = BIT(len(sorted_nums))
        result = [0] * len(nums)

        # Process from right to left
        for i in range(len(nums) - 1, -1, -1):
            r = rank[nums[i]]
            result[i] = bit.query(r - 1)  # Count smaller elements
            bit.update(r, 1)  # Add current element

        return result

    def countSmallerSegmentTree(self, nums):
        """
        Alternative approach using Segment Tree
        """
        if not nums:
            return []

        # Coordinate compression
        sorted_nums = sorted(set(nums))
        rank = {num: i for i, num in enumerate(sorted_nums)}

        class SegmentTree:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (4 * n)

            def update(self, index, val, node=1, start=0, end=None):
                if end is None:
                    end = self.n - 1

                if start == end:
                    self.tree[node] += val
                    return

                mid = (start + end) // 2
                if index <= mid:
                    self.update(index, val, 2 * node, start, mid)
                else:
                    self.update(index, val, 2 * node + 1, mid + 1, end)

                self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

            def query(self, left, right, node=1, start=0, end=None):
                if end is None:
                    end = self.n - 1

                if right < start or left > end:
                    return 0

                if left <= start and right >= end:
                    return self.tree[node]

                mid = (start + end) // 2
                return self.query(left, right, 2 * node, start, mid) + self.query(
                    left, right, 2 * node + 1, mid + 1, end
                )

        st = SegmentTree(len(sorted_nums))
        result = [0] * len(nums)

        # Process from right to left
        for i in range(len(nums) - 1, -1, -1):
            r = rank[nums[i]]
            result[i] = st.query(0, r - 1)  # Count smaller elements
            st.update(r, 1)  # Add current element

        return result


def test_count_smaller():
    """Test cases for Count of Smaller Numbers After Self"""
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [5, 2, 6, 1]
    result1 = solution.countSmaller(nums1)
    expected1 = [2, 1, 1, 0]
    assert result1 == expected1

    result1_bst = solution.countSmallerBST(nums1)
    assert result1_bst == expected1

    result1_bit = solution.countSmallerBinaryIndexedTree(nums1)
    assert result1_bit == expected1

    result1_st = solution.countSmallerSegmentTree(nums1)
    assert result1_st == expected1

    # Test case 2: All same numbers
    nums2 = [1, 1, 1, 1]
    result2 = solution.countSmaller(nums2)
    expected2 = [0, 0, 0, 0]
    assert result2 == expected2

    # Test case 3: Strictly decreasing
    nums3 = [4, 3, 2, 1]
    result3 = solution.countSmaller(nums3)
    expected3 = [3, 2, 1, 0]
    assert result3 == expected3

    # Test case 4: Strictly increasing
    nums4 = [1, 2, 3, 4]
    result4 = solution.countSmaller(nums4)
    expected4 = [0, 0, 0, 0]
    assert result4 == expected4

    # Test case 5: Single element
    nums5 = [1]
    result5 = solution.countSmaller(nums5)
    expected5 = [0]
    assert result5 == expected5

    # Test case 6: Empty array
    nums6 = []
    result6 = solution.countSmaller(nums6)
    expected6 = []
    assert result6 == expected6

    print("All test cases passed!")


if __name__ == "__main__":
    test_count_smaller()
