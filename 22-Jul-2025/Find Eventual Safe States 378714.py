# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False  
            if state[node] == 2:
                return True   

            state[node] = 1  

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2  
            return True

        return [i for i in range(n) if dfs(i)]