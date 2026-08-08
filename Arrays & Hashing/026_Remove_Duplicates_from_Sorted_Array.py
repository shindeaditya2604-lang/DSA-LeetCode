"""
LeetCode 26 - Remove Duplicates from Sorted Array

Pattern:
Two Pointers

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i+1


               
        
