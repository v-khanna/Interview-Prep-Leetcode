"""
Validate Binary Search Tree (Medium)
https://leetcode.com/problems/validate-binary-search-tree/

Problem: Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Example:
Input: root = [2,1,3]
Output: true

Approach: Inorder traversal with bounds checking
Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        """
        Validate BST using inorder traversal
        """

        def inorder(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            return inorder(node.left, lower, node.val) and inorder(
                node.right, node.val, upper
            )

        return inorder(root)

    def isValidBSTInorder(self, root):
        """
        Validate BST using inorder traversal with list
        """

        def inorder(node):
            if not node:
                return []

            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)
        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False

        return True

    def isValidBSTIterative(self, root):
        """
        Iterative inorder traversal
        """
        if not root:
            return True

        stack = []
        prev = float("-inf")
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if curr.val <= prev:
                return False

            prev = curr.val
            curr = curr.right

        return True

    def isValidBSTRecursive(self, root):
        """
        Recursive approach with bounds
        """

        def isValid(node, min_val, max_val):
            if not node:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            return isValid(node.left, min_val, node.val) and isValid(
                node.right, node.val, max_val
            )

        return isValid(root, float("-inf"), float("inf"))

    def isValidBSTMorris(self, root):
        """
        Morris inorder traversal (constant space)
        """
        if not root:
            return True

        prev = float("-inf")
        curr = root

        while curr:
            if not curr.left:
                if curr.val <= prev:
                    return False
                prev = curr.val
                curr = curr.right
            else:
                # Find inorder predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if curr.val <= prev:
                        return False
                    prev = curr.val
                    curr = curr.right

        return True


def test_validate_binary_search_tree():
    """Test cases for Validate Binary Search Tree"""
    solution = Solution()

    # Test case 1: Valid BST
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    assert solution.isValidBST(root1) == True
    assert solution.isValidBSTInorder(root1) == True
    assert solution.isValidBSTIterative(root1) == True
    assert solution.isValidBSTRecursive(root1) == True
    assert solution.isValidBSTMorris(root1) == True

    # Test case 2: Invalid BST
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    assert solution.isValidBST(root2) == False
    assert solution.isValidBSTInorder(root2) == False
    assert solution.isValidBSTIterative(root2) == False
    assert solution.isValidBSTRecursive(root2) == False
    assert solution.isValidBSTMorris(root2) == False

    # Test case 3: Single node
    root3 = TreeNode(1)
    assert solution.isValidBST(root3) == True
    assert solution.isValidBSTInorder(root3) == True
    assert solution.isValidBSTIterative(root3) == True
    assert solution.isValidBSTRecursive(root3) == True
    assert solution.isValidBSTMorris(root3) == True

    # Test case 4: Empty tree
    root4 = None
    assert solution.isValidBST(root4) == True
    assert solution.isValidBSTInorder(root4) == True
    assert solution.isValidBSTIterative(root4) == True
    assert solution.isValidBSTRecursive(root4) == True
    assert solution.isValidBSTMorris(root4) == True

    # Test case 5: Duplicate values (invalid)
    root5 = TreeNode(1)
    root5.left = TreeNode(1)
    assert solution.isValidBST(root5) == False
    assert solution.isValidBSTInorder(root5) == False
    assert solution.isValidBSTIterative(root5) == False
    assert solution.isValidBSTRecursive(root5) == False
    assert solution.isValidBSTMorris(root5) == False

    # Test case 6: Large valid BST
    root6 = TreeNode(10)
    root6.left = TreeNode(5)
    root6.right = TreeNode(15)
    root6.left.left = TreeNode(3)
    root6.left.right = TreeNode(7)
    root6.right.left = TreeNode(12)
    root6.right.right = TreeNode(18)
    assert solution.isValidBST(root6) == True
    assert solution.isValidBSTInorder(root6) == True
    assert solution.isValidBSTIterative(root6) == True
    assert solution.isValidBSTRecursive(root6) == True
    assert solution.isValidBSTMorris(root6) == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_validate_binary_search_tree()
