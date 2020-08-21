### 345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
#### Python
#### Time Limit Exceeded
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        v={'a','e','i','o','u','A','E','I','O','U'}
        L=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if L[i] not in v:
                i=i+1
            if L[j] not in v:
                j=j-1
            if L[i] in v and L[j] in v:
                L[i],L[j]=L[j],L[i]
                
        return ''.join(L)
```
#### Csharp
```csharp
public class Solution {
    public string ReverseVowels(string s) {
        char[] v = new char[] { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };
        int i = 0;
        int j = s.Length - 1;
        char[] ss = s.ToCharArray();
        while (i < j)
        {
            if (v.Contains(ss[i]) && v.Contains(ss[j]))
            {
                char t = ss[i];
                ss[i] = ss[j];
                ss[j] = t;
                i++;
                j--;
            }
            else
            {
                if (!v.Contains(ss[i])) i++;
                if (!v.Contains(ss[j])) j--;
            }
        }
        return new string(ss);    
    }
}
```