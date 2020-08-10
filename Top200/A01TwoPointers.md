# Two pointers

#### two-sum-ii-input-array-is-sorted
[Leetcode No167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers== None: return None
        i = 0
        j = len(numbers)-1
        while i!=j:
            if numbers[i]+numbers[j]>target:
                j=j-1
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                return [i+1,j+1]
        return None
```
</details>

#### sum-of-square-numbers
[Leetcode No633](https://leetcode.com/problems/sum-of-square-numbers/)  

<details>
  <summary>Solution</summary>

```python
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<0: return False
        i=0
        j=int(math.sqrt(c))
        while i<=j:
            if pow(i,2)+pow(j,2)==c:
                return True
            elif pow(i,2)+pow(j,2)>c:
                j=j-1
            else:
                i=i+1
        return False  
```
</details>

#### reverse-vowels-of-a-string
[Leetcode No345](https://leetcode.com/problems/reverse-vowels-of-a-string/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        v={'a','e','i','o','u','A','E','I','O','U'}
        L=list(s)
        result=[]
        i=0
        j=len(s)-1
        while i<j:
            # find vowel from right
            while j>=0 and L[j] not in v:
                j-=1
            # find vowel from left
            while i<j and L[i] not in v:
                i+=1
            if i<j:
                L[i], L[j]=L[j], L[i]
            i+=1
            j-=1
                
        return ''.join(L)
```
</details>

#### valid-palindrome-ii
[Leetcode No680](https://leetcode.com/problems/valid-palindrome-ii/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def isPalindrome(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i=i+1
            j=j-1
        return True
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return self.isPalindrome(s,i+1,j) or self.isPalindrome(s,i,j-1)
            i=i+1
            j=j-1
        return True
```
</details>

#### merge-sorted-array
[Leetcode No88](https://leetcode.com/problems/merge-sorted-array/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1;
        while i >= 0 or j >= 0:
            if i < 0:
                nums1[k] = nums2[j]
                j=j-1
            elif j < 0:
                nums1[k] = nums1[i]
                i=i-1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i=i-1
            else:
                nums1[k] = nums2[j]
                j=j-1
            k=k-1
```
</details>

#### linked-list-cycle
[Leetcode No141](https://leetcode.com/problems/linked-list-cycle/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        l1 = head
        l2 = head.next
        while l1 and l2 and l2.next :
            if l1 == l2: 
                return True
            l1 = l1.next
            l2 = l2.next.next
        return False
```
</details>

#### longest-word-in-dictionary-through-deleting
[Leetcode No524](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)  

<details>
  <summary>Solution</summary>
  
```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longestWord = ""
        for target in d:
            l1 = len(longestWord)
            l2 = len(target)
            if l1 > l2 or (l1 == l2 and longestWord < target):
                continue
            if self.isSubstr(s, target):       
                longestWord = target

        return longestWord

    def isSubstr(self,s, target):
        i = 0
        j = 0
        while i < len(s) and j < len(target):
            if s[i] == target[j]:
                j=j+1
            i=i+1
        return j == len(target)
```
</details>