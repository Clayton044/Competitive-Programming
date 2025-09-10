# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer=[]
        s= set()

        for num in nums:
            if num in s:
                answer.append(num)
            else:
                s.add(num)
        return answer