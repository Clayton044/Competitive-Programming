# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        email_to_name = {}
        #this took wayyy tooo long, and yes I did use AI a bit :D
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in parent:
                    parent[email] = email
                union(account[1], email)
        
        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)
        
        return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]