### 633. Sum of Square Numbers
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: 3
Output: False
#### Python
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
```csharp
public class Solution {
    public bool JudgeSquareSum(int c) {
        if (c<0){
            return false;
        }
        int i = 0;
        int j = Convert.ToInt32(Math.Sqrt(c));
        while(i<=j){
            if(Math.Pow(i,2)+Math.Pow(j,2)==c)
                return true;
            else if(Math.Pow(i,2)+Math.Pow(j,2)<c)
                i=i+1;
            else j=j-1;
        
        }
        return false;
    }
}
```
### Time Complexity O(sqrt(c)), Space Complexity O(1)
