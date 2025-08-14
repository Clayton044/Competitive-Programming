# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
    
        return [num for num, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]