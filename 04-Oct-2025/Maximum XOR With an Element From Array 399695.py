# Problem: Maximum XOR With an Element From Array - https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted([(m, x, i) for i, (x, m) in enumerate(queries)])
        
        ans = [0] * len(queries)
        trie = {}
        idx = 0
        
        def insert(num):
            node = trie
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
        def query(num):
            if not trie:
                return -1
            node = trie
            res = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit
                if toggled in node:
                    res |= (1 << i)
                    node = node[toggled]
                elif bit in node:
                    node = node[bit]
                else:
                    return -1
            return res
        
        for m, x, i in queries:
            while idx < len(nums) and nums[idx] <= m:
                insert(nums[idx])
                idx += 1
            ans[i] = query(x)
        
        return ans