# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses


        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1


        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return taken == numCourses