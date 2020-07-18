### 524. Longest Word in Dictionary through Deleting
 Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"

Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"

Note:

    All the strings in the input will only contain lower-case letters.
    The size of the dictionary won't exceed 1,000.
    The length of all the strings in the input won't exceed 1,000.
#### Python
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
#### Csharp
```csharp
public class Solution {
    public string FindLongestWord(string s, IList<string> d) {
        String longestWord = "";
        foreach (String target in d) {
            int l1 = longestWord.Length, l2 = target.Length;
            if (l1 > l2 || (l1 == l2 && longestWord.CompareTo(target) < 0)) {
                continue;
            }
            //add this if isSubstr is public
            if (isSubstr(s, target)) {         
                longestWord = target;
            }
        }
        return longestWord;
    }
    private bool isSubstr(String s, String target) {
        int i = 0, j = 0;
        while (i < s.Length && j < target.Length) {
            if (s[i] == target[j]) {
                j++;
            }
            i++;
        }
        return j == target.Length;
    }
}
```