from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        currentSum = 0

        for i in range(k):
            currentSum += nums[i]

        maxSum = currentSum

        for i in range(k, len(nums)):
            currentSum = currentSum + nums[i] - nums[i - k]

            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum / k
