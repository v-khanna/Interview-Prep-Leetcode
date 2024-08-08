class Solution:
    def twoSum(self, nums, target):
        n = len(nums)  # Get the length of the list
        for i in range(n):  # Outer loop to pick the first number
            for j in range(i + 1, n):  # Inner loop to pick the second number
                if nums[i] + nums[j] == target:  # Check if the sum equals the target
                    return [i, j]  # If found, return the indices
        return []  # Return an empty list if no solution is found
