# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)

       
        substrings = []
        for word in arr:
            subs = set()
            for i in range(len(word)):
                for j in range(i+1, len(word)+1):
                    subs.add(word[i:j])
            substrings.append(subs)
            # print(word[i])

        result = []
        for i in range(n):
            candidates = []
            for sub in substrings[i]:
                unique = True
                for j in range(n):
                    if i != j and sub in substrings[j]:
                        unique = False
                        # print(substrings[j])
                        break
                if unique:
                    candidates.append(sub)
            if not candidates:
                result.append("")
            else:
                result.append(min(candidates, key=lambda x: (len(x), x)))
        return result