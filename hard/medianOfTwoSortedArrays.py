from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # Partition nums1
            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            # Find the elements around the partition
            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float("inf") if partitionX == m else nums1[partitionX]

            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float("inf") if partitionY == n else nums2[partitionY]

            # Check if partition is correct
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1

        return 0.0


# Alternative solution using merge approach (simpler but less efficient)
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the arrays
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Add remaining elements
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        # Find median
        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    # Test case 1
    nums1 = [1, 3]
    nums2 = [2]
    result1 = solution.findMedianSortedArrays(nums1, nums2)
    result1_alt = solution2.findMedianSortedArrays(nums1, nums2)
    print(
        f"Median of {nums1} and {nums2}: {result1} (binary search), {result1_alt} (merge)"
    )
    # Expected: 2.0

    # Test case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result2 = solution.findMedianSortedArrays(nums1, nums2)
    result2_alt = solution2.findMedianSortedArrays(nums1, nums2)
    print(
        f"Median of {nums1} and {nums2}: {result2} (binary search), {result2_alt} (merge)"
    )
    # Expected: 2.5

    # Test case 3
    nums1 = [0, 0]
    nums2 = [0, 0]
    result3 = solution.findMedianSortedArrays(nums1, nums2)
    result3_alt = solution2.findMedianSortedArrays(nums1, nums2)
    print(
        f"Median of {nums1} and {nums2}: {result3} (binary search), {result3_alt} (merge)"
    )
    # Expected: 0.0
