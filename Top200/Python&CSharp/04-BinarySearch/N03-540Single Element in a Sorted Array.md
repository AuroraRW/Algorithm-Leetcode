### 540. Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
#### Python
```python
# Time complexity: O(logN)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        while l<h:
            m = l + (h - l) // 2
            if m % 2 == 1:
                m=m-1 # the result must be even index
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                h = m
        return nums[l]
```
```python
# Time complexity: O(N)
from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        dic = dict(Counter(nums))
        for i in dic:
            if dic[i] == 1:
                return i
```
#### Csharp
```csharp
```

