# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        i = 2
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1 if i * i == n else 2
        return count == 3