from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the array to use two pointers

        for i in range(len(nums) - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"3Sum for {nums1}: {result1}")
    # Expected: [[-1,-1,2], [-1,0,1]]

    # Test case 2
    nums2 = []
    result2 = solution.threeSum(nums2)
    print(f"3Sum for {nums2}: {result2}")
    # Expected: []

    # Test case 3
    nums3 = [0]
    result3 = solution.threeSum(nums3)
    print(f"3Sum for {nums3}: {result3}")
    # Expected: []

    # Test case 4
    nums4 = [0, 0, 0]
    result4 = solution.threeSum(nums4)
    print(f"3Sum for {nums4}: {result4}")
    # Expected: [[0, 0, 0]]
