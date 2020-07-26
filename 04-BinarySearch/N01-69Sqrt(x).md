### 69. Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
#### Python
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
#### Csharp
```csharp
```