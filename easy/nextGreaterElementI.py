"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Build next greater element map for nums2
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Find next greater for nums1
        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # Output: [-1,3,-1]
    print(solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))  # Output: [3,-1]
