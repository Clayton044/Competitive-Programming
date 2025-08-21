# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        res =[1]

        for i in range(rowIndex):

            next_row =[0] * (len(res)+1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row
        return res
            