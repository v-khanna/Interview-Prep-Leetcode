"""
Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Problem: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

Approach: Hash set
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        Check for duplicates using hash set
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

    def containsDuplicateSort(self, nums):
        """
        Check for duplicates using sorting
        """
        nums_sorted = sorted(nums)

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1]:
                return True

        return False

    def containsDuplicateSet(self, nums):
        """
        Check for duplicates using set length comparison
        """
        return len(nums) != len(set(nums))

    def containsDuplicateBruteForce(self, nums):
        """
        Brute force approach with nested loops
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

    def containsDuplicateOptimized(self, nums):
        """
        Optimized version with early termination
        """
        if len(nums) <= 1:
            return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


def test_contains_duplicate():
    """Test cases for Contains Duplicate"""
    solution = Solution()

    # Test case 1: Contains duplicates
    nums1 = [1, 2, 3, 1]
    assert solution.containsDuplicate(nums1) == True
    assert solution.containsDuplicateSort(nums1) == True
    assert solution.containsDuplicateSet(nums1) == True
    assert solution.containsDuplicateBruteForce(nums1) == True
    assert solution.containsDuplicateOptimized(nums1) == True

    # Test case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums2) == False
    assert solution.containsDuplicateSort(nums2) == False
    assert solution.containsDuplicateSet(nums2) == False
    assert solution.containsDuplicateBruteForce(nums2) == False
    assert solution.containsDuplicateOptimized(nums2) == False

    # Test case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solution.containsDuplicate(nums3) == True
    assert solution.containsDuplicateSort(nums3) == True
    assert solution.containsDuplicateSet(nums3) == True
    assert solution.containsDuplicateBruteForce(nums3) == True
    assert solution.containsDuplicateOptimized(nums3) == True

    # Test case 4: Empty array
    nums4 = []
    assert solution.containsDuplicate(nums4) == False
    assert solution.containsDuplicateSort(nums4) == False
    assert solution.containsDuplicateSet(nums4) == False
    assert solution.containsDuplicateBruteForce(nums4) == False
    assert solution.containsDuplicateOptimized(nums4) == False

    # Test case 5: Single element
    nums5 = [1]
    assert solution.containsDuplicate(nums5) == False
    assert solution.containsDuplicateSort(nums5) == False
    assert solution.containsDuplicateSet(nums5) == False
    assert solution.containsDuplicateBruteForce(nums5) == False
    assert solution.containsDuplicateOptimized(nums5) == False

    # Test case 6: Two identical elements
    nums6 = [1, 1]
    assert solution.containsDuplicate(nums6) == True
    assert solution.containsDuplicateSort(nums6) == True
    assert solution.containsDuplicateSet(nums6) == True
    assert solution.containsDuplicateBruteForce(nums6) == True
    assert solution.containsDuplicateOptimized(nums6) == True

    # Test case 7: Large array with duplicates
    nums7 = list(range(1000)) + [999]
    assert solution.containsDuplicate(nums7) == True
    assert solution.containsDuplicateSort(nums7) == True
    assert solution.containsDuplicateSet(nums7) == True
    assert solution.containsDuplicateOptimized(nums7) == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_contains_duplicate()
