# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for a, b in allowedSwaps:
            parent[find(a)] = find(b)
        
        #this took way tooooo long, and I 200% used AI.

        components = {}
        for i in range(n):
            root = find(i)
            if root not in components:
                components[root] = [{}, {}]
            src_freq, tgt_freq = components[root]
            src_freq[source[i]] = src_freq.get(source[i], 0) + 1
            tgt_freq[target[i]] = tgt_freq.get(target[i], 0) + 1
        
        matches = 0
        for src_freq, tgt_freq in components.values():
            for val, cnt in src_freq.items():
                matches += min(cnt, tgt_freq.get(val, 0))
        
        return n - matches