"""
Clone Graph (Hard)
https://leetcode.com/problems/clone-graph/

Problem: Given a reference of a node in a connected undirected graph, return a deep copy of the graph.

Example:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Approach: DFS/BFS with hash map for visited nodes
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        """
        Clone graph using DFS with memoization
        """
        if not node:
            return None

        # Hash map to store visited nodes
        visited = {}

        def dfs(original_node):
            # If node already visited, return its clone
            if original_node in visited:
                return visited[original_node]

            # Create new node
            clone_node = Node(original_node.val)
            visited[original_node] = clone_node

            # Clone all neighbors
            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))

            return clone_node

        return dfs(node)

    def cloneGraphBFS(self, node):
        """
        Clone graph using BFS
        """
        if not node:
            return None

        # Hash map to store visited nodes
        visited = {}
        queue = deque([node])

        # Create clone of the first node
        visited[node] = Node(node.val)

        while queue:
            original_node = queue.popleft()
            clone_node = visited[original_node]

            # Process all neighbors
            for neighbor in original_node.neighbors:
                if neighbor not in visited:
                    # Create clone of neighbor
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add neighbor to clone's neighbors
                clone_node.neighbors.append(visited[neighbor])

        return visited[node]

    def cloneGraphIterative(self, node):
        """
        Iterative DFS approach
        """
        if not node:
            return None

        # Hash map to store visited nodes
        visited = {}
        stack = [node]

        # Create clone of the first node
        visited[node] = Node(node.val)

        while stack:
            original_node = stack.pop()
            clone_node = visited[original_node]

            # Process all neighbors
            for neighbor in original_node.neighbors:
                if neighbor not in visited:
                    # Create clone of neighbor
                    visited[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                # Add neighbor to clone's neighbors
                clone_node.neighbors.append(visited[neighbor])

        return visited[node]

    def cloneGraphWithValidation(self, node):
        """
        Clone graph with additional validation
        """
        if not node:
            return None

        # Hash map to store visited nodes
        visited = {}

        def dfs(original_node):
            # If node already visited, return its clone
            if original_node in visited:
                return visited[original_node]

            # Validate node
            if not hasattr(original_node, "val") or not hasattr(
                original_node, "neighbors"
            ):
                raise ValueError("Invalid node structure")

            # Create new node
            clone_node = Node(original_node.val)
            visited[original_node] = clone_node

            # Clone all neighbors
            if original_node.neighbors:
                for neighbor in original_node.neighbors:
                    if neighbor is not None:
                        clone_node.neighbors.append(dfs(neighbor))

            return clone_node

        return dfs(node)


def create_test_graph():
    """Helper function to create a test graph"""
    # Create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Set neighbors
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    return node1


def test_clone_graph():
    """Test cases for Clone Graph"""
    solution = Solution()

    # Test case 1: Basic graph
    original = create_test_graph()
    cloned = solution.cloneGraph(original)

    # Verify structure
    assert cloned.val == 1
    assert len(cloned.neighbors) == 2
    assert cloned.neighbors[0].val == 2
    assert cloned.neighbors[1].val == 4

    # Verify it's a deep copy (different objects)
    assert cloned is not original
    assert cloned.neighbors[0] is not original.neighbors[0]

    # Test BFS approach
    cloned_bfs = solution.cloneGraphBFS(original)
    assert cloned_bfs.val == 1
    assert len(cloned_bfs.neighbors) == 2

    # Test iterative approach
    cloned_iter = solution.cloneGraphIterative(original)
    assert cloned_iter.val == 1
    assert len(cloned_iter.neighbors) == 2

    # Test case 2: Single node
    single_node = Node(1)
    cloned_single = solution.cloneGraph(single_node)
    assert cloned_single.val == 1
    assert len(cloned_single.neighbors) == 0
    assert cloned_single is not single_node

    # Test case 3: Empty graph
    assert solution.cloneGraph(None) is None
    assert solution.cloneGraphBFS(None) is None
    assert solution.cloneGraphIterative(None) is None

    # Test case 4: Self-loop
    loop_node = Node(1)
    loop_node.neighbors = [loop_node]
    cloned_loop = solution.cloneGraph(loop_node)
    assert cloned_loop.val == 1
    assert len(cloned_loop.neighbors) == 1
    assert cloned_loop.neighbors[0] == cloned_loop  # Self-reference

    print("All test cases passed!")


if __name__ == "__main__":
    test_clone_graph()
