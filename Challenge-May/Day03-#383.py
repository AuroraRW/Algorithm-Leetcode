"""
Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
You may assume that both strings contain only lowercase letters.
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if magazine includes ransomNote, then Counter(ransomNote) - Counter(magazine) has nothing
        return not len(Counter(ransomNote) - Counter(magazine))


if __name__ == "__main__":
    S = Solution()
    print(S.canConstruct('ac', 'aab'))