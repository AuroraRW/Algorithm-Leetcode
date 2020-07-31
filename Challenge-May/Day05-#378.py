"""
First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.


Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] = (-1, i)
            else:
                dic[s[i]] = (1, i)
        for (v1, v2) in dic.values():
            if v1 == 1:
                return v2
        return -1


class Solution1:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


if __name__ == "__main__":
    S = Solution1()
    print(S.firstUniqChar("aadadaad"))