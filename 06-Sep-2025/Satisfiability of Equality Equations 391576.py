# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = list(range(26))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for eq in equations:
            if eq[1] == '=':
                x, y = ord(eq[0]) - 97, ord(eq[3]) - 97
                union(x, y)
        
        for eq in equations:
            if eq[1] == '!':
                x, y = ord(eq[0]) - 97, ord(eq[3]) - 97
                if find(x) == find(y):
                    return False
        return True