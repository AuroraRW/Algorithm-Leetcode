### 680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
#### Python
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
#### Csharp
```csharp
public class Solution {
    public bool ValidPalindrome(string s)
    {
        int i = 0;
        int j = s.Length-1;
        while (i<j)
        {
            if (s[i] != s[j])
                return isPalindrome(s, i + 1, j) || isPalindrome(s, i, j - 1);
            i++;
            j--;
        }
        return true;
    }
    public bool isPalindrome(string s, int i, int j)
    {
        while(i < j)
        {
            if (s[i] != s[j])
                return false;
            i = i + 1;
            j = j - 1;
        }
        return true;
    }
}
```
