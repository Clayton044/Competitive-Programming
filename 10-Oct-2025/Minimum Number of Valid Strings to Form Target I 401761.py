# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

    def get_prefix_lengths(self, s):
        lengths = []
        node = self.root
        for i, ch in enumerate(s):
            if ch not in node.children:
                break
            node = node.children[ch]
            lengths.append(i + 1)
        return lengths        
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        n = len(target)
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == INF:
                continue
            prefix_lengths = trie.get_prefix_lengths(target[i:])
            for L in prefix_lengths:
                dp[i + L] = min(dp[i + L], dp[i] + 1)
        
        return dp[n] if dp[n] != INF else -1