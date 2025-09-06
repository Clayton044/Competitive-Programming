# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum=int(a,base =2) + int(b,base=2)
        return bin(sum)[2:] 