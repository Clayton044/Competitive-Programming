# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        n1, n2 = len(nums1), len(nums2) 
        heap = []
        for i in range(min(k, n1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        result = []
        while heap and len(result) < k:
            s, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return result