"""
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
"""

from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Cycle detected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge

        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # [2,3]
    print(
        solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
    )  # [1,4]
