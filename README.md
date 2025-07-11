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

### Easy Problems (15 problems)

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

12. **Friend Circles** (`friendCircles.py`)
    - Count connected components using Union Find
    - Time Complexity: O(n²)
    - Space Complexity: O(n)

13. **Next Greater Element I** (`nextGreaterElementI.py`)
    - Find next greater element using monotonic stack
    - Time Complexity: O(n)
    - Space Complexity: O(n)

14. **Number of 1 Bits** (`numberOf1Bits.py`)
    - Count set bits using bit manipulation
    - Time Complexity: O(log n)
    - Space Complexity: O(1)

15. **Climbing Stairs** (`climbingStairs.py`)
    - Count ways to climb stairs with 1 or 2 steps at a time
    - Time Complexity: O(n)
    - Space Complexity: O(1)

### Medium Problems (27 problems)

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

5. **Binary Tree Level Order Traversal** (`binaryTreeLevelOrderTraversal.py`)
   - Traverse binary tree level by level
   - Time Complexity: O(n)
   - Space Complexity: O(n)

6. **Course Schedule** (`courseSchedule.py`)
   - Check if courses can be completed (cycle detection)
   - Time Complexity: O(V + E)
   - Space Complexity: O(V + E)

7. **Subsets** (`subsets.py`)
   - Generate all possible subsets (power set)
   - Time Complexity: O(n * 2^n)
   - Space Complexity: O(n * 2^n)

8. **Top K Frequent Elements** (`topKFrequentElements.py`)
   - Find k most frequent elements
   - Time Complexity: O(n log k)
   - Space Complexity: O(n)

9. **Group Anagrams** (`groupAnagrams.py`)
   - Group strings by anagram
   - Time Complexity: O(n * k log k)
   - Space Complexity: O(n * k)

10. **Kth Smallest Element in BST** (`kthSmallestElementInBST.py`)
    - Find kth smallest element in binary search tree
    - Time Complexity: O(k)
    - Space Complexity: O(h)

11. **Number of Islands** (`numberOfIslands.py`)
    - Count connected components in 2D grid
    - Time Complexity: O(m * n)
    - Space Complexity: O(m * n)

12. **Spiral Matrix** (`spiralMatrix.py`)
    - Traverse matrix in spiral order
    - Time Complexity: O(m * n)
    - Space Complexity: O(1)

13. **Rotate Image** (`rotateImage.py`)
    - Rotate matrix 90 degrees clockwise
    - Time Complexity: O(n²)
    - Space Complexity: O(1)

14. **Search in Rotated Sorted Array** (`searchInRotatedSortedArray.py`)
    - Binary search in rotated sorted array
    - Time Complexity: O(log n)
    - Space Complexity: O(1)

15. **Letter Combinations of Phone Number** (`letterCombinationsOfPhoneNumber.py`)
    - Generate all letter combinations for phone number
    - Time Complexity: O(4^n * n)
    - Space Complexity: O(4^n * n)

16. **Combination Sum** (`combinationSum.py`)
    - Find all combinations that sum to target
    - Time Complexity: O(n^(target/min))
    - Space Complexity: O(target/min)

17. **Permutations** (`permutations.py`)
    - Generate all permutations of array
    - Time Complexity: O(n!)
    - Space Complexity: O(n!)

18. **Minimum Path Sum** (`minimumPathSum.py`)
    - Find minimum path sum in grid
    - Time Complexity: O(m * n)
    - Space Complexity: O(m * n)

19. **Unique Paths** (`uniquePaths.py`)
    - Count unique paths in grid
    - Time Complexity: O(m * n)
    - Space Complexity: O(m * n)

20. **Redundant Connection** (`redundantConnection.py`)
    - Detect cycle in undirected graph using Union Find
    - Time Complexity: O(n)
    - Space Complexity: O(n)

21. **Next Greater Element II** (`nextGreaterElementII.py`)
    - Find next greater element in circular array
    - Time Complexity: O(n)
    - Space Complexity: O(n)

22. **Daily Temperatures** (`dailyTemperatures.py`)
    - Find days to wait for warmer temperature
    - Time Complexity: O(n)
    - Space Complexity: O(n)

23. **Range Sum Query - Immutable** (`rangeSumQueryImmutable.py`)
    - Range sum queries using prefix sum
    - Time Complexity: O(1) per query
    - Space Complexity: O(n)

24. **Power of Two** (`powerOfTwo.py`)
    - Check if number is power of 2 using bit manipulation
    - Time Complexity: O(1)
    - Space Complexity: O(1)

25. **Longest Substring Without Repeating Characters** (`longestSubstringWithoutRepeatingCharacters.py`)
    - Find longest substring without repeating characters
    - Time Complexity: O(n)
    - Space Complexity: O(min(m, n))

26. **House Robber** (`houseRobber.py`)
    - Maximum money robbed without robbing adjacent houses
    - Time Complexity: O(n)
    - Space Complexity: O(1)

27. **Longest Common Subsequence** (`longestCommonSubsequence.py`)
    - Find length of longest common subsequence between two strings
    - Time Complexity: O(m * n)
    - Space Complexity: O(m * n)

### Hard Problems (62 problems)

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

4. **LFU Cache** (`lfuCache.py`)
   - Design Least Frequently Used cache with O(1) operations
   - Time Complexity: O(1) for get/put
   - Space Complexity: O(capacity)

5. **Word Ladder II** (`wordLadderII.py`)
   - Find all shortest transformation sequences
   - Time Complexity: O(n * 26^l * l)
   - Space Complexity: O(n * l)

6. **N-Queens II** (`nQueensII.py`)
   - Count all valid n-queens solutions
   - Time Complexity: O(n!)
   - Space Complexity: O(n)

7. **Trapping Rain Water II** (`trappingRainWaterII.py`)
   - 2D water trapping with min-heap
   - Time Complexity: O(mn * log(mn))
   - Space Complexity: O(mn)

8. **Edit Distance** (`editDistance.py`)
   - Classic DP with path reconstruction
   - Time Complexity: O(mn)
   - Space Complexity: O(mn)

9. **Serialize and Deserialize Binary Tree** (`serializeAndDeserializeBinaryTree.py`)
   - Tree serialization and deserialization
   - Time Complexity: O(n)
   - Space Complexity: O(n)

10. **Binary Tree Maximum Path Sum** (`binaryTreeMaximumPathSum.py`)
    - Find maximum path sum in binary tree
    - Time Complexity: O(n)
    - Space Complexity: O(h)

11. **Longest Consecutive Sequence** (`longestConsecutiveSequence.py`)
    - Find longest consecutive sequence using hash set
    - Time Complexity: O(n)
    - Space Complexity: O(n)

12. **Word Break** (`wordBreak.py`)
    - Check if string can be segmented into dictionary words
    - Time Complexity: O(n²)
    - Space Complexity: O(n)

13. **Longest Increasing Subsequence** (`longestIncreasingSubsequence.py`)
    - Find longest increasing subsequence with binary search
    - Time Complexity: O(n log n)
    - Space Complexity: O(n)

14. **Coin Change** (`coinChange.py`)
    - Minimum coins to make amount (unbounded knapsack)
    - Time Complexity: O(amount * len(coins))
    - Space Complexity: O(amount)

15. **Partition Equal Subset Sum** (`partitionEqualSubsetSum.py`)
    - Check if array can be partitioned into equal sums
    - Time Complexity: O(n * sum/2)
    - Space Complexity: O(sum/2)

16. **Longest Palindromic Substring** (`longestPalindromicSubstring.py`)
    - Find longest palindromic substring
    - Time Complexity: O(n²)
    - Space Complexity: O(1)

17. **Valid Sudoku** (`validSudoku.py`)
    - Validate 9x9 Sudoku board
    - Time Complexity: O(n²)
    - Space Complexity: O(n)

18. **Implement Trie** (`implementTrie.py`)
    - Implement trie data structure
    - Time Complexity: O(m) for insert/search
    - Space Complexity: O(ALPHABET_SIZE * m * n)

19. **Word Search** (`wordSearch.py`)
    - Find word in 2D grid using backtracking
    - Time Complexity: O(mn * 4^L)
    - Space Complexity: O(L)

20. **Remove Invalid Parentheses** (`removeInvalidParentheses.py`)
    - Remove minimum parentheses to make valid
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)

21. **Merge Intervals** (`mergeIntervals.py`)
    - Merge overlapping intervals
    - Time Complexity: O(n log n)
    - Space Complexity: O(n)

22. **Trapping Rain Water II** (`trappingRainWaterII.py`)
    - 2D water trapping with min-heap
    - Time Complexity: O(mn * log(mn))
    - Space Complexity: O(mn)

23. **Edit Distance** (`editDistance.py`)
    - Classic DP with path reconstruction
    - Time Complexity: O(mn)
    - Space Complexity: O(mn)

24. **Number of Islands II** (`numberOfIslandsII.py`)
    - Dynamic island counting using Union Find
    - Time Complexity: O(k * log(mn))
    - Space Complexity: O(mn)

25. **Range Sum Query - Mutable** (`rangeSumQueryMutable.py`)
    - Range sum with updates using Segment Tree
    - Time Complexity: O(log n) per query/update
    - Space Complexity: O(n)

26. **Range Sum Query 2D** (`rangeSumQuery2D.py`)
    - 2D range sum queries using prefix sum
    - Time Complexity: O(1) per query
    - Space Complexity: O(mn)

27. **Word Search II** (`wordSearchII.py`)
    - Multiple word search using Trie
    - Time Complexity: O(mn * 4^L)
    - Space Complexity: O(L)

28. **Sliding Window Maximum** (`slidingWindowMaximum.py`)
    - Maximum in sliding window using monotonic deque
    - Time Complexity: O(n)
    - Space Complexity: O(k)

29. **Single Number III** (`singleNumberIII.py`)
    - Find two single numbers using bit manipulation
    - Time Complexity: O(n)
    - Space Complexity: O(1)

30. **Design Add and Search Words Data Structure** (`designAddAndSearchWordsDataStructure.py`)
    - Trie with wildcard support
    - Time Complexity: O(m) for add, O(26^m) for search
    - Space Complexity: O(ALPHABET_SIZE * m * n)

31. **Implement Trie (Prefix Tree)** (`implementTriePrefixTree.py`)
    - Basic trie implementation
    - Time Complexity: O(m) for insert/search
    - Space Complexity: O(ALPHABET_SIZE * m * n)

32. **Minimum Window Substring** (`minimumWindowSubstring.py`)
    - Minimum window containing all characters
    - Time Complexity: O(n)
    - Space Complexity: O(k)

33. **Alien Dictionary** (`alienDictionary.py`)
    - Find the order of characters in an alien language
    - Time Complexity: O(V + E)
    - Space Complexity: O(V + E)

34. **Basic Calculator** (`basicCalculator.py`)
    - Evaluate a basic arithmetic expression with parentheses
    - Time Complexity: O(n)
    - Space Complexity: O(n)

35. **Basic Calculator II** (`basicCalculatorII.py`)
    - Evaluate a basic arithmetic expression with +, -, *, /
    - Time Complexity: O(n)
    - Space Complexity: O(n)

36. **Best Time to Buy and Sell Stock III** (`bestTimeToBuyAndSellStockIII.py`)
    - Max profit with at most two transactions
    - Time Complexity: O(n)
    - Space Complexity: O(1)

37. **Best Time to Buy and Sell Stock IV** (`bestTimeToBuyAndSellStockIV.py`)
    - Max profit with at most k transactions
    - Time Complexity: O(n * k)
    - Space Complexity: O(k)

38. **Burst Balloons** (`burstBalloons.py`)
    - Max coins from bursting balloons
    - Time Complexity: O(n³)
    - Space Complexity: O(n²)

39. **Candy** (`candy.py`)
    - Distribute candies to children with ratings
    - Time Complexity: O(n)
    - Space Complexity: O(n)

40. **Clone Graph** (`cloneGraph.py`)
    - Deep copy of a connected undirected graph
    - Time Complexity: O(V + E)
    - Space Complexity: O(V)

41. **Concatenated Words** (`concatenatedWords.py`)
    - Find all concatenated words in a dictionary
    - Time Complexity: O(n * L²)
    - Space Complexity: O(n * L)

42. **Count of Smaller Numbers After Self** (`countOfSmallerNumbersAfterSelf.py`)
    - Count smaller numbers after each element
    - Time Complexity: O(n log n)
    - Space Complexity: O(n)

43. **Data Stream as Disjoint Intervals** (`dataStreamAsDisjointIntervals.py`)
    - Summarize a data stream as disjoint intervals
    - Time Complexity: O(log n) for addNum, O(n) for getIntervals
    - Space Complexity: O(n)

44. **Largest Rectangle in Histogram** (`largestRectangleInHistogram.py`)
    - Find largest rectangle area in histogram using monotonic stack
    - Time Complexity: O(n)
    - Space Complexity: O(n)

45. **Longest Valid Parentheses** (`longestValidParentheses.py`)
    - Find longest valid parentheses substring
    - Time Complexity: O(n)
    - Space Complexity: O(n)

46. **Maximal Rectangle** (`maximalRectangle.py`)
    - Find largest rectangle containing only 1's in binary matrix
    - Time Complexity: O(mn)
    - Space Complexity: O(n)

47. **Word Break II** (`wordBreakII.py`)
    - Find all possible word break combinations
    - Time Complexity: O(n³ + 2^n)
    - Space Complexity: O(2^n)

48. **Sudoku Solver** (`sudokuSolver.py`)
    - Solve Sudoku puzzle using backtracking
    - Time Complexity: O(9^(n²))
    - Space Complexity: O(n²)

49. **Alien Dictionary** (`alienDictionary.py`)
    - Find the order of characters in an alien language
    - Time Complexity: O(C) where C is total number of characters
    - Space Complexity: O(1) since alphabet size is fixed

50. **Concatenated Words** (`concatenatedWords.py`)
    - Find all concatenated words in a dictionary
    - Time Complexity: O(n * L²)
    - Space Complexity: O(n * L)

51. **Expression Add Operators** (`expressionAddOperators.py`)
    - Add operators to create expressions that evaluate to target
    - Time Complexity: O(4^n)
    - Space Complexity: O(n)

52. **Word Search II** (`wordSearchII.py`)
    - Multiple word search using Trie and DFS
    - Time Complexity: O(m * n * 4^L) where L is max word length
    - Space Complexity: O(k * L) where k is number of words

53. **Remove Invalid Parentheses** (`removeInvalidParentheses.py`)
    - Remove minimum parentheses to make valid using BFS
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)

## How to Use

1. **Run Individual Problems:**
   ```bash
   python easy/two-sum.py
   python easy/climbingStairs.py
   python medium/addTwoNumbers.py
   python medium/houseRobber.py
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
- **Sliding Window**: Used in "Longest Substring Without Repeating Characters", "Minimum Window Substring", "Sliding Window Maximum"
- **Dynamic Programming**: Used in "Climbing Stairs", "Regular Expression Matching", "Minimum Path Sum", "Unique Paths", "Edit Distance", "Word Break", "Longest Increasing Subsequence", "Coin Change", "Partition Equal Subset Sum", "House Robber", "Longest Common Subsequence"
- **Binary Search**: Used in "Median of Two Sorted Arrays", "Search in Rotated Sorted Array", "Kth Smallest Element in BST", "Longest Increasing Subsequence"
- **Heap/Priority Queue**: Used in "Merge k Sorted Lists", "Top K Frequent Elements", "Trapping Rain Water II"
- **Stack**: Used in "Valid Parentheses"
- **Monotonic Stack/Queue**: Used in "Next Greater Element I/II", "Daily Temperatures", "Sliding Window Maximum"
- **Union Find/Disjoint Set**: Used in "Friend Circles", "Redundant Connection", "Number of Islands II"
- **Segment Tree**: Used in "Range Sum Query - Mutable", "Range Sum Query 2D"
- **Trie**: Used in "Implement Trie", "Word Search II", "Design Add and Search Words"
- **Bit Manipulation**: Used in "Single Number III", "Power of Two", "Number of 1 Bits"
- **Backtracking**: Used in "Subsets", "Permutations", "Combination Sum", "Letter Combinations", "N-Queens II", "Word Search", "Remove Invalid Parentheses"
- **Graph/Tree Traversal**: Used in "Binary Tree Level Order Traversal", "Number of Islands", "Course Schedule", "Binary Tree Maximum Path Sum", "Serialize and Deserialize Binary Tree"
- **Hash Map/Set**: Used in "Group Anagrams", "Two Sum", "Longest Consecutive Sequence", "Valid Sudoku"
- **Matrix Manipulation**: Used in "Spiral Matrix", "Rotate Image", "Word Search"
- **Design**: Used in "LFU Cache", "Implement Trie"
- **String Manipulation**: Used in "Longest Palindromic Substring", "Remove Invalid Parentheses"
- **Interval Problems**: Used in "Merge Intervals"
- **Prefix Sum**: Used in "Range Sum Query - Immutable", "Range Sum Query 2D"

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