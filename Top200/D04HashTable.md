# Hash Table

#### two-sum 
[Leetcode No1](https://leetcode.com/problems/two-sum/)
<details>
  <summary>Solution</summary>

```python
# dictionary:{value: index}
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        for i in range(len(nums)):
            if target-nums[i] in d.keys():
                return [i, d[target-nums[i]]]
            else:
                d[nums[i]]=i
```
</details>

#### contains-duplicate 
[Leetcode No217](https://leetcode.com/problems/contains-duplicate/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d= dict()
        for i in nums:
            if i in d:
                return True
            else:
                d[i]=1
        return False
```
</details>

#### longest-harmonious-subsequence 
[Leetcode No594](https://leetcode.com/problems/longest-harmonious-subsequence/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = dict(Counter(nums))
        n = set(nums)
        longest = 0
        for i in n:
            if i + 1 in d:
                longest = max(longest, d[i] + d[i + 1])
        return longest
```
</details>

#### longest-consecutive-sequence
[Leetcode No128](https://leetcode.com/problems/longest-consecutive-sequence/)
<details>
  <summary>Solution</summary>

```python

```
</details>
