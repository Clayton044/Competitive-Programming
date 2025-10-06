# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution(object):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.endNode = False

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()

        def insert(self, word):
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Solution.TrieNode()
                curr = curr.children[c]
            curr.endNode = True

    def longestWord(self, words):
        trie = self.Trie()
        for w in words:
            trie.insert(w)
        self.best = ""

        def dfs(node, path):
            if node is trie.root or node.endNode:
                word = "".join(path)
                if len(word) > len(self.best) or (len(word) == len(self.best) and word < self.best):
                    self.best = word
                for ch in sorted(node.children.keys()):
                    child = node.children[ch]
                    if child.endNode:
                        path.append(ch)
                        dfs(child, path)
                        path.pop()

        dfs(trie.root, [])
        return self.best