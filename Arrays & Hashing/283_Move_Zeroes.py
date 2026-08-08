"""
LeetCode 283 - Move Zeroes

Pattern:
Two Pointers

Time Complexity:
O(n)

Space Complexity:
O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j]  = nums[j], nums[i]
                j += 1

    
        
        
