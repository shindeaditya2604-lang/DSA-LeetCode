"""
LeetCode 347 - Top K Frequent Elements

Pattern:
Bucket Sort

Time Complexity:
O(n)

Space Complexity:
O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        bucket = [[] for i in range(len(nums)+1)]
        for num,freq in count.items():

            bucket[freq].append(num)
        ans = []
        for i in range(len(bucket)-1,-1,-1):

            for num in  bucket[i]:
                
                ans.append(num)

            if len(ans) == k:
                return ans        
