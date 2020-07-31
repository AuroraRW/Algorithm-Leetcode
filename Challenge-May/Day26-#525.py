"""
Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        numsDic = dict()
        result = 0
        s=0
        for i in range(len(nums)):
            if nums[i] > 0:
                s += 1
            else:
                s -= 1

            if s == 0:
                result=i+1
            elif s in numsDic.keys():
                result=max(result, i-numsDic[ s])
            else:
                numsDic[s] = i

        return result
