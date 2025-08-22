# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        
        answer = [-1] * n
        answer[0] = 0  
        
        
        
        queue = deque()
        queue.append((0, 0, 0))  
        queue.append((0, 1, 0))  
        
        
        visited = {(0, 0), (0, 1)}
        
        while queue:
            node, last_color, steps = queue.popleft()
            
            
            if last_color == 0:
                next_graph = blue_graph
                next_color = 1
            else:  
                next_graph = red_graph
                next_color = 0
            
            for neighbor in next_graph[node]:
                if (neighbor, next_color) not in visited:
                    visited.add((neighbor, next_color))
                    queue.append((neighbor, next_color, steps + 1))
                    
                    
                    if answer[neighbor] == -1:
                        answer[neighbor] = steps + 1
        
        return answer