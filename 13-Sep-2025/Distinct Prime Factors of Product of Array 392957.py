# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        for num in nums:
            d = 2
            while d * d <= num:
                if num % d == 0:
                    primes.add(d)
                    while num % d == 0:
                        num //= d
                d += 1
            if num > 1:
                primes.add(num)
        return len(primes)