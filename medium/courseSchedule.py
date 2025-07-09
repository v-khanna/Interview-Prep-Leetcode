"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Some courses may have prerequisites. Return true if you can finish all courses.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))  # True
    print(solution.canFinish(2, [[1, 0], [0, 1]]))  # False
