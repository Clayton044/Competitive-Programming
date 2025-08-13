# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        idx = {r: i for i, r in enumerate(recipes)}
        adj = defaultdict(list)

        need = [0] * len(recipes)
        for i, ing_list in enumerate(ingredients):
            need[i] = len(ing_list)
            for ing in ing_list:
                adj[ing].append(recipes[i])

        supplies_set = set(supplies)
        q = deque(supplies)        
        processed = set()          
        made = set()               
        res = []
        
        for r in recipes:
            if r in supplies_set:
                made.add(r)
                res.append(r)
        while q:
            item = q.popleft()
            if item in processed:
                continue
            processed.add(item)

            for rec in adj.get(item, ()):
                i = idx[rec]
                need[i] -= 1
                if need[i] == 0 and rec not in made:
                    made.add(rec)
                    res.append(rec)
                    q.append(rec)  

        return res