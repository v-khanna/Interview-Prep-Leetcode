"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            # Update max sum including current node
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)

            # Return max path sum that can be extended by parent
            return node.val + max(left_sum, right_sum)

        dfs(root)
        return self.max_sum


# Test cases
if __name__ == "__main__":
    # Build tree: [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    solution = Solution()
    print(solution.maxPathSum(root))  # Output: 6

    # Build tree: [-10,9,20,null,null,15,7]
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)

    print(solution.maxPathSum(root2))  # Output: 42
