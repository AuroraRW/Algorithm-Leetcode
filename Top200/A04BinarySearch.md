# Binary Search

## Introduction

## Questions
#### sqrtx 
[Leetcode No69](https://leetcode.com/problems/sqrtx/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        h=x
        while l<=h:
            m=l+(h-l)//2
            sqrt=x//m
            if sqrt==m:
                return sqrt
            elif sqrt<m:
                h=m-1
            else:
                l=m+1
        return h # the last interval makes h lower than l
```
</details>

#### find-smallest-letter-greater-than-target 
[Leetcode No744](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = 0
        h = n - 1
        while l <= h:
            m = l + (h - l) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                h = m - 1
        if l<n:
            return letters[l]
        else:
            return letters[0]
```
</details>

#### single-element-in-a-sorted-array 
[Leetcode No540](https://leetcode.com/problems/single-element-in-a-sorted-array/)
<details>
  <summary>Solution</summary>

```python
# Time complexity: O(logN)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        while l<h:
            m = l + (h - l) // 2
            if m % 2 == 1:
                m=m-1 # the result must be even index
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                h = m
        return nums[l]
```
```python
# Time complexity: O(N)
from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dic = dict(Counter(nums))
        for i in dic:
            if dic[i] == 1:
                return i
```

</details>

#### first-bad-version 
[Leetcode No278](https://leetcode.com/problems/first-bad-version/)
<details>
  <summary>Solution</summary>
  
```python
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        h=n
        while l<=h:
            m=l+(h-l)//2
            if isBadVersion(m)==True:
                h=m-1
            else:
                l=m+1
        return l
```
</details>

#### find-minimum-in-rotated-sorted-array 
[Leetcode No153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
<details>
  <summary>Solution</summary>

</details>

#### find-first-and-last-position-of-element-in-sorted-array 
[Leetcode No34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
<details>
  <summary>Solution</summary>

</details>


