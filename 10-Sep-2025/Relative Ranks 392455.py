# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
        ans = [""] * len(score)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, (idx, _) in enumerate(sorted_scores):
            if i < 3:
                ans[idx] = medals[i]
            else:
                ans[idx] = str(i + 1)
        return ans