"""
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells.
"""

from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        grid = [[0] * n for _ in range(m)]
        result = []

        for i, j in positions:
            if grid[i][j] == 1:
                result.append(uf.count)
                continue

            grid[i][j] = 1
            uf.count += 1
            pos = i * n + j

            # Check all 4 directions
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    uf.union(pos, ni * n + nj)

            result.append(uf.count)

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))  # [1,1,2,3]
