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
# it is one to one mapping. that means s map to t, t map to s
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d=dict()
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
            else:
                if d[s[i]]!=t[i]:
                    return False
        d=dict()
        for i in range(len(t)):
            if t[i] not in d:
                d[t[i]]=s[i]
            else:
                if d[t[i]]!=s[i]:
                    return False
        
        return True
```
</details>

#### palindromic-substrings 
[Leetcode No647](https://leetcode.com/problems/palindromic-substrings/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # single letter is palindromic substring
            count+=1
            # when the length of palindromic substring is odd
            left=i-1
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            # when the length of palindromic substring is even
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        return count
```
</details>

#### palindrome-number 
[Leetcode No9](https://leetcode.com/problems/palindrome-number/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1=str(x)
        s2=s1[::-1]
        return s1==s2
```
</details>

#### count-binary-substrings 
[Leetcode No696](https://leetcode.com/problems/count-binary-substrings/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur=1
        result=[]
        # get the length of consecutive substring
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cur+=1
            else:
                result.append(cur)
                cur=1
        result.append(cur)
        r=0
        
        for x,y in zip(result[:],result[1:]):
            r+=min(x,y)   
        return r
```
</details>