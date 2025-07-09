class Solution:
    def hasDuplicate(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


def main():
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    result = solution.hasDuplicate(nums)
    print(f"Array has duplicates: {result}")

    # Test case 2
    nums2 = [1, 2, 3, 4, 5]
    result2 = solution.hasDuplicate(nums2)
    print(f"Array has duplicates: {result2}")


if __name__ == "__main__":
    main()
