### 605. Can Place Flowers
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.
#### Python
```python
# find triple zero
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed=[0]+flowerbed+[0]
        result=0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0:
                result=result+1
                flowerbed[i]=1
        return result>=n
```
#### Csharp
```csharp
public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        int len = flowerbed.Length;
        int result = 0;
        int pre=0;
        int next=0;
        for (int i = 0; i < len; i++) {
            if (flowerbed[i] == 1) {
                continue;
            }
            //int pre = i == 0 ? 0 : flowerbed[i - 1];
            if (i==0) pre=0;
            else pre=flowerbed[i-1];
            //int next = i == len - 1 ? 0 : flowerbed[i + 1];
            if (i==len-1) next=0;
            else next=flowerbed[i+1];
                
            if (pre == 0 && next == 0) {
                result++;
                flowerbed[i] = 1;
            }
        }
        return result >= n;
    }
}
```
