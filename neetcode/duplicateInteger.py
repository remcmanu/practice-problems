# Neetcode : Duplicate Integer
# 7-12-2024
# @remcmanu

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

example_1 = [1, 2, 3, 3]
example_2 = [1, 2, 3, 4]

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # use a HASHSET to store distinct items with a .contains time complexity of O(1)
        # in other words, better than an array for this purpose
        hashset = set()
        
        for item in nums:
            if item in hashset:
                return True
            hashset.add (item)
        return False

# needed to instatiate class with (), i.e. Solution(), otherwise: "Solution.hasDuplicate() missing 1 required positional argument: 'nums'"
if Solution().hasDuplicate (example_1) and not Solution().hasDuplicate (example_2):
    print ("passed")