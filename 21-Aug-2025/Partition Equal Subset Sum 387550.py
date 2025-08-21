# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
    
    
        if total % 2 == 1:
            return False
        
        target = total // 2
        if max(nums) > target:
            return False  
        
        
        dp = set([0])  
        
        for num in nums:
            
            new_sums = {num + x for x in dp if num + x <= target}
            dp.update(new_sums)
            
            if target in dp:
                return True  
        
        return target in dp 