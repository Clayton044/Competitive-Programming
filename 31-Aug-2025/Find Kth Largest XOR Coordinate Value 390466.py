# Problem: Find Kth Largest XOR Coordinate Value - https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/description/?envType=problem-list-v2&envId=bit-manipulation

import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        values = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (matrix[i-1][j-1] ^
                                prefix[i-1][j] ^
                                prefix[i][j-1] ^
                                prefix[i-1][j-1])
                values.append(prefix[i][j])

        # Use heapq.nlargest for efficiency instead of full sort
        return heapq.nlargest(k, values)[-1]