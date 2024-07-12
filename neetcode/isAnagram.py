# Neetcode : Is Anagram
# 7-12-2024
# @remcmanu

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


# Test Cases
s1 = "racecar" 
t1 = "carrace"
s2 = "jar"
t2 = "jam"

import time

class MySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if sorted(s) == sorted(t): return True
        else: return False

start = time.time()
result = MySolution().isAnagram(s1, t1) and not MySolution().isAnagram(s2, t2)
end = time.time()
if result: 
    print ("MySolution passed" + str(end-start))

class OfficialSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

start = time.time()
result = OfficialSolution().isAnagram(s1, t1) and not OfficialSolution().isAnagram(s2, t2)
end = time.time()
if result: 
    print ("OfficialSolution passed" + str(end-start))

# official solution uses a dictionary and iterates through the strings, keeping a running count of every character. 
# This is 2 * O(n) with the final comparison, whereas sorting first is O(log n) + O(n)
# So the two solutions are both O(n)