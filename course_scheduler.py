class Solution:
    def canFinish(self, numCourses, prerequisites):
        from collections import deque

        # Build graph and in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken_courses = 0

        while queue:
            course = queue.popleft()
            taken_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return taken_courses == numCourses
