"""
Construct Binary Tree from Preorder and Inorder Traversal (Medium)
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem: Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Approach: Recursive with hash map
Time Complexity: O(n)
Space Complexity: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        """
        Build binary tree from preorder and inorder traversals
        """
        if not preorder or not inorder:
            return None

        # Create hash map for O(1) lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            # Root is always the first element in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find root position in inorder
            root_idx = inorder_map[root_val]

            # Calculate left subtree size
            left_size = root_idx - in_start

            # Recursively build left and right subtrees
            root.left = build(
                pre_start + 1, pre_start + left_size, in_start, root_idx - 1
            )
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTreeIterative(self, preorder, inorder):
        """
        Iterative approach using stack
        """
        if not preorder or not inorder:
            return None

        # Create hash map
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])

            if inorder_map[preorder[i]] < inorder_map[stack[-1].val]:
                # Current node is left child
                stack[-1].left = node
            else:
                # Current node is right child
                while stack and inorder_map[preorder[i]] > inorder_map[stack[-1].val]:
                    last_node = stack.pop()
                    inorder_idx += 1

                last_node.right = node

            stack.append(node)

        return root

    def buildTreeOptimized(self, preorder, inorder):
        """
        Optimized version with better space usage
        """
        if not preorder or not inorder:
            return None

        # Create hash map
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            if pre_start == pre_end:
                return root

            root_idx = inorder_map[root_val]
            left_size = root_idx - in_start

            root.left = build(
                pre_start + 1, pre_start + left_size, in_start, root_idx - 1
            )
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def buildTreeWithValidation(self, preorder, inorder):
        """
        Version with input validation
        """
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None

        # Check if arrays contain same elements
        if set(preorder) != set(inorder):
            return None

        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            root_idx = inorder_map[root_val]
            left_size = root_idx - in_start

            root.left = build(
                pre_start + 1, pre_start + left_size, in_start, root_idx - 1
            )
            root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)


def treeToArray(root):
    """Helper function to convert tree to array (level order)"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)

        result.extend(level)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def test_construct_binary_tree():
    """Test cases for Construct Binary Tree from Preorder and Inorder Traversal"""
    solution = Solution()

    # Test case 1: Basic case
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    result1 = solution.buildTree(preorder1, inorder1)
    expected1 = [3, 9, 20, None, None, 15, 7]
    assert treeToArray(result1) == expected1

    result1_iter = solution.buildTreeIterative(preorder1, inorder1)
    assert treeToArray(result1_iter) == expected1

    result1_opt = solution.buildTreeOptimized(preorder1, inorder1)
    assert treeToArray(result1_opt) == expected1

    result1_val = solution.buildTreeWithValidation(preorder1, inorder1)
    assert treeToArray(result1_val) == expected1

    # Test case 2: Single node
    preorder2 = [1]
    inorder2 = [1]
    result2 = solution.buildTree(preorder2, inorder2)
    expected2 = [1]
    assert treeToArray(result2) == expected2

    # Test case 3: Left skewed tree
    preorder3 = [1, 2, 3]
    inorder3 = [3, 2, 1]
    result3 = solution.buildTree(preorder3, inorder3)
    expected3 = [1, 2, None, 3]
    assert treeToArray(result3) == expected3

    # Test case 4: Right skewed tree
    preorder4 = [1, 2, 3]
    inorder4 = [1, 2, 3]
    result4 = solution.buildTree(preorder4, inorder4)
    expected4 = [1, None, 2, None, None, None, 3]
    assert treeToArray(result4) == expected4

    # Test case 5: Empty arrays
    preorder5 = []
    inorder5 = []
    result5 = solution.buildTree(preorder5, inorder5)
    assert result5 is None

    # Test case 6: Different lengths (invalid input)
    preorder6 = [1, 2]
    inorder6 = [1]
    result6 = solution.buildTreeWithValidation(preorder6, inorder6)
    assert result6 is None

    print("All test cases passed!")


if __name__ == "__main__":
    test_construct_binary_tree()
