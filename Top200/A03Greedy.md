# Greedy

#### assign-cookies
[Leetcode No455](https://leetcode.com/problems/assign-cookies/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g==None or s==None:
            return 0;
        g.sort()
        s.sort()
        gi=0
        si=0
        while gi<len(g) and si<len(s):
            if g[gi]<=s[si]:
                gi=gi+1
            si=si+1
        return gi
```
</details>

#### non-overlapping-intervals
[Leetcode No435](https://leetcode.com/problems/non-overlapping-intervals/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0]) # if sort by end then remove the one with smaller start
        res=0
        pre=0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[pre][1]: # remove
                res=res+1
                if (intervals[i][1] < intervals[pre][1]): # remove the one with bigger end
                    pre = i
            else:
                pre = i
        return res
```
</details>

#### minimum-number-of-arrows-to-burst-balloons
[Leetcode No452](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])# sort by end
        res=1
        pre=0
        for i in range(1, len(points)):
            if points[i][0] > points[pre][1]:
                res=res+1
                pre = i
                
        return res
```
</details>

#### queue-reconstruction-by-height
[Leetcode No406](https://leetcode.com/problems/queue-reconstruction-by-height/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
```
</details>

#### best-time-to-buy-and-sell-stock
[Leetcode No121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        soFarMin = prices[0]
        m = 0
        for i in range(len(prices)):
            if soFarMin > prices[i]:
                soFarMin = prices[i]
            else:
                m = max(m, prices[i] - soFarMin)
        return m
```
</details>

#### best-time-to-buy-and-sell-stock-ii
[Leetcode No122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                result = result + prices[i] - prices[i-1]
        return result
```
</details>

#### can-place-flowers
[Leetcode No605](https://leetcode.com/problems/can-place-flowers/)  

<details>
  <summary>Solution</summary>

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
</details>

#### is-subsequence
[Leetcode No392](https://leetcode.com/problems/is-subsequence/)  

<details>
  <summary>Solution</summary>

Difference between Subsequence and Substring
```python
# traversal t to see if s is done
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            if t[ti] == s[si]:
                si += 1
            ti += 1
        return si == len(s)
```
```python
# queue
import collections
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q= deque(s)
        for c in t:
            if not q: return True
            if c == q[0]:
                q.popleft()
        return not q
```
</details>

#### non-decreasing-array
[Leetcode No665](https://leetcode.com/problems/non-decreasing-array/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                cnt=cnt+1
                if i==0 or nums[i-1]<nums[i+1]:
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
            if cnt>1:
                break
        return cnt<2
```
</details>

#### maximum-subarray
[Leetcode No53](https://leetcode.com/problems/maximum-subarray/)  

<details>
  <summary>Solution</summary>

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums==None or len(nums)==0:
            return 0
        presum=nums[0]
        maxsum=presum
        for i in range(1,len(nums)):
            if presum<0: 
                presum=nums[i]
            else:
                presum=presum+nums[i]
            maxsum=max(maxsum, presum)
        return maxsum
```
</details>

#### partition-labels
[Leetcode No763](https://leetcode.com/problems/partition-labels/)  

<details>
  <summary>Solution</summary>

</details>
