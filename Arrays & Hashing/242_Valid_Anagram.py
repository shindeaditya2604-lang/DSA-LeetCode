"""
LeetCode 242 - Valid Anagram

Pattern:
HashMap
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for ch in s:
            if ch in countS:
                countS[ch] += 1
            else:
                countS[ch] = 1
        
        for ch in t:
            if ch in countT:
                countT[ch] += 1
            else:
                countT[ch] = 1

        return countS == countT

        
