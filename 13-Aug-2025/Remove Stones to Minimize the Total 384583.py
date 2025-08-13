# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            
            new_val = largest - largest // 2  
            heapq.heappush(max_heap, -new_val)

        
        return -sum(max_heap)