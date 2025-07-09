# LeetCode Practice Repository

A comprehensive collection of LeetCode problems organized by difficulty level with complete solutions and test cases.

## Repository Structure

```
Interview-Prep-Leetcode/
├── easy/           # Easy problems (1-2 star difficulty)
├── medium/         # Medium problems (3-4 star difficulty)
├── hard/           # Hard problems (5 star difficulty)
└── README.md       # This file
```

## Problems by Difficulty

### Easy Problems (9 problems)

1. **Two Sum** (`two-sum.py`)
   - Find two numbers in an array that add up to a target
   - Time Complexity: O(n²)
   - Space Complexity: O(1)

2. **Move Zeroes** (`moveZeroes.py`)
   - Move all zeros to the end while maintaining relative order
   - Time Complexity: O(n)
   - Space Complexity: O(1)

3. **Find Pivot Index** (`findPivotIndex.py`)
   - Find the pivot index where left sum equals right sum
   - Time Complexity: O(n)
   - Space Complexity: O(1)

4. **Maximum Average Subarray I** (`maxAvgSubarray1.py`)
   - Find maximum average of subarray of length k
   - Time Complexity: O(n)
   - Space Complexity: O(1)

5. **Contains Duplicate** (`duplicateInteger.py`)
   - Check if array contains any duplicates
   - Time Complexity: O(n²)
   - Space Complexity: O(1)

6. **Find the Highest Altitude** (`highestAltitude.py`)
   - Find the highest altitude from gain array
   - Time Complexity: O(n)
   - Space Complexity: O(1)

7. **Is Subsequence** (`isSubsequence.py`)
   - Check if s is a subsequence of t
   - Time Complexity: O(n)
   - Space Complexity: O(1)

8. **Merge Strings Alternately** (`mergeStringsAlternatively.py`)
   - Merge two strings alternately
   - Time Complexity: O(max(len(word1), len(word2)))
   - Space Complexity: O(n)

9. **GCD of Strings** (`gcdOfStrings.py`)
   - Find the largest string that divides both strings
   - Time Complexity: O(min(len(str1), len(str2)))
   - Space Complexity: O(1)

10. **Valid Parentheses** (`validParentheses.py`)
    - Check if parentheses are valid
    - Time Complexity: O(n)
    - Space Complexity: O(n)

11. **Palindrome Number** (`palindromeNumber.py`)
    - Check if a number is a palindrome
    - Time Complexity: O(log n)
    - Space Complexity: O(1)

### Medium Problems (5 problems)

1. **Add Two Numbers** (`addTwoNumbers.py`)
   - Add two numbers represented by linked lists
   - Time Complexity: O(max(len(l1), len(l2)))
   - Space Complexity: O(max(len(l1), len(l2)))

2. **Longest Substring Without Repeating Characters** (`longestSubstringWithoutRepeating.py`)
   - Find longest substring without repeating characters
   - Time Complexity: O(n)
   - Space Complexity: O(min(m, n))

3. **Container With Most Water** (`containerWithMostWater.py`)
   - Find container with maximum water capacity
   - Time Complexity: O(n)
   - Space Complexity: O(1)

4. **3Sum** (`threeSum.py`)
   - Find all unique triplets that sum to zero
   - Time Complexity: O(n²)
   - Space Complexity: O(1)

### Hard Problems (3 problems)

1. **Median of Two Sorted Arrays** (`medianOfTwoSortedArrays.py`)
   - Find median of two sorted arrays
   - Time Complexity: O(log(min(m, n)))
   - Space Complexity: O(1)

2. **Regular Expression Matching** (`regularExpressionMatching.py`)
   - Match string against regular expression pattern
   - Time Complexity: O(mn)
   - Space Complexity: O(mn)

3. **Merge k Sorted Lists** (`mergeKSortedLists.py`)
   - Merge k sorted linked lists
   - Time Complexity: O(n log k)
   - Space Complexity: O(k)

## How to Use

1. **Run Individual Problems:**
   ```bash
   python easy/two-sum.py
   python medium/addTwoNumbers.py
   python hard/medianOfTwoSortedArrays.py
   ```

2. **Study Patterns:**
   - Each file contains the problem solution with multiple approaches
   - Test cases are included to verify correctness
   - Time and space complexity analysis is provided

3. **Practice Strategy:**
   - Start with easy problems to build confidence
   - Move to medium problems to learn common patterns
   - Attempt hard problems to master advanced algorithms

## Common Algorithm Patterns

- **Two Pointers**: Used in problems like "Container With Most Water", "3Sum"
- **Sliding Window**: Used in "Longest Substring Without Repeating Characters"
- **Dynamic Programming**: Used in "Regular Expression Matching"
- **Binary Search**: Used in "Median of Two Sorted Arrays"
- **Heap/Priority Queue**: Used in "Merge k Sorted Lists"
- **Stack**: Used in "Valid Parentheses"

## Tips for Interview Preparation

1. **Understand the Problem**: Read carefully and ask clarifying questions
2. **Plan Your Approach**: Think about time/space complexity before coding
3. **Code Cleanly**: Write readable, well-structured code
4. **Test Thoroughly**: Include edge cases in your test scenarios
5. **Optimize**: Look for ways to improve your solution
6. **Practice Regularly**: Consistency is key to improvement

## Contributing

Feel free to add more problems, improve existing solutions, or add alternative approaches. Make sure to:
- Include test cases
- Add complexity analysis
- Follow the existing code structure
- Update this README with new problems

## Resources

- [LeetCode](https://leetcode.com/) - Practice platform
- [LeetCode Discuss](https://leetcode.com/discuss/) - Community solutions
- [LeetCode Solutions](https://github.com/azl397985856/leetcode) - Comprehensive solutions

Happy coding! 🚀 