"""
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "null"
        return (
            str(root.val)
            + ","
            + self.serialize(root.left)
            + ","
            + self.serialize(root.right)
        )

    def deserialize(self, data):
        """Decodes your encoded data to tree."""

        def helper(nodes):
            if not nodes:
                return None
            val = nodes.popleft()
            if val == "null":
                return None
            root = TreeNode(int(val))
            root.left = helper(nodes)
            root.right = helper(nodes)
            return root

        nodes = deque(data.split(","))
        return helper(nodes)


# Test cases
if __name__ == "__main__":
    codec = Codec()
    # Build tree: [1,2,3,null,null,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    serialized = codec.serialize(root)
    print(f"Serialized: {serialized}")
    deserialized = codec.deserialize(serialized)
    print(f"Deserialized root value: {deserialized.val}")
