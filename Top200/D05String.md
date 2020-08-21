# String

#### valid-anagram 
[Leetcode No242](https://leetcode.com/problems/valid-anagram/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs=Counter(s)
        ct=Counter(t)
        if cs==ct:
            return True
        return False
```
</details>

#### longest-palindrome 
[Leetcode No409](https://leetcode.com/problems/longest-palindrome/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=Counter(s)
        result=0
        odd=0
        for i in d:
            if d[i] %2==0:
                result+=d[i]
            else:
                result+=d[i]-1
                # there is odd number
                odd=1     
        return result+odd
```
```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=Counter(s)
        result=0
        for i in d:
            result+=d[i] //2 *2
        # there is odd number
        if result< len(s):
            result+=1
                
        return result
```
</details>

#### isomorphic-strings 
[Leetcode No205](https://leetcode.com/problems/isomorphic-strings/)
<details>
  <summary>Solution</summary>

```python

```
</details>

#### palindromic-substrings 
[Leetcode No647](https://leetcode.com/problems/palindromic-substrings/)
<details>
  <summary>Solution</summary>

```python
```
</details>

#### palindrome-number 
[Leetcode No9](https://leetcode.com/problems/palindrome-number/)
<details>
  <summary>Solution</summary>

```python
```
</details>

#### count-binary-substrings 
[Leetcode No696](https://leetcode.com/problems/count-binary-substrings/)
<details>
  <summary>Solution</summary>

```python
```
</details>