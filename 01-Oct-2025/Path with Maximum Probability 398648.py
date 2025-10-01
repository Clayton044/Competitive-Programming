# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))
        
        prob = [0.0] * n
        prob[start_node] = 1.0
        heap = [(-1.0, start_node)]  
        
        while heap:
            neg_p, u = heapq.heappop(heap)
            current_p = -neg_p
            
            if u == end_node:
                return current_p
                
            if current_p < prob[u]:
                continue
                
            for v, p_edge in graph[u]:
                new_prob = current_p * p_edge
                if new_prob > prob[v]:
                    prob[v] = new_prob
                    heapq.heappush(heap, (-new_prob, v))
                    
        return 0.0