# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
    
        result = []
        min_heap = []  
        
        time = 0
        idx = 0  
        n = len(tasks)
        
        while idx < n or min_heap:
            
            while idx < n and sorted_tasks[idx][0] <= time:
                et, pt, original_idx = sorted_tasks[idx]
                heapq.heappush(min_heap, (pt, original_idx))
                idx += 1
            
            
            if not min_heap:
                time = sorted_tasks[idx][0]  
            else:
                
                processing_time, original_idx = heapq.heappop(min_heap)
                result.append(original_idx)
                time += processing_time
        
        return result