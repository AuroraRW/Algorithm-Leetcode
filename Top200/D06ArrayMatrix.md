# Array Matrix

#### move-zeroes 
[Leetcode No283](https://leetcode.com/problems/move-zeroes/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt=0
        i=0
        while i < len(nums):
            if nums[i]==0:
                nums.pop(i)
                cnt+=1
                i=0
            else:
                i=i+1

        for i in range(cnt):
            nums.append(0)
```
```python
# i stop at the zero, j move on, and then exchange
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N = len(nums)
        i = 0
        for j in range(N):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
```
</details>

#### reshape-the-matrix 
[Leetcode No566](https://leetcode.com/problems/reshape-the-matrix/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row=len(nums)
        column=len(nums[0])
        if row*column != r*c:
            return nums
        result=[]
        temp=[]
        for i in range(row):
            for j in range(column):
                temp.append(nums[i][j])
                if len(temp)==c:
                    result.append(temp)
                    temp=[]  
                
        return result
```
```python
# using index
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row=len(nums)
        column=len(nums[0])
        if row*column != r*c:
            return nums
        result=[]
        for i in range(r):
            result.append([0]*c)
        newRow=0
        newCol=0
        for i in range(row):
            for j in range(column):
                if newCol == c:
                    # next row
                    newRow+=1
                    newCol=0
                result[newRow][newCol]=nums[i][j]
                newCol+=1
        return result
```
</details>

#### max-consecutive-ones 
[Leetcode No485](https://leetcode.com/problems/max-consecutive-ones/)
<details>
  <summary>Solution</summary>
  
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        onesNum=0
        MaxNum=0
        for n in nums:
            if n==1:
                onesNum+=1
            MaxNum=max(MaxNum, onesNum)
            if n==0:
                onesNum=0
        return MaxNum
```
</details>

#### search-a-2d-matrix-ii 
[Leetcode No240](https://leetcode.com/problems/search-a-2d-matrix-ii/)
<details>
  <summary>Solution</summary>
  
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row=len(matrix)
        col=len(matrix[0])
        # start from the left-top corner
        r=0
        c=col-1
        while r < row and c>=0:
            if target>matrix[r][c]:
                r=r+1
            elif target<matrix[r][c]:
                c=c-1
            else:
                return True
            
        return False
```
</details>

#### kth-smallest-element-in-a-sorted-matrix 
[Leetcode No378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>

#### set-mismatch 
[Leetcode No645](https://leetcode.com/problems/set-mismatch/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>

#### find-the-duplicate-number
[Leetcode No287](https://leetcode.com/problems/find-the-duplicate-number/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>

#### beautiful-arrangement-ii 
[Leetcode No667](https://leetcode.com/problems/beautiful-arrangement-ii/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>

#### degree-of-an-array 
[Leetcode No697](https://leetcode.com/problems/degree-of-an-array/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>

#### toeplitz-matrix 
[Leetcode No766](https://leetcode.com/problems/toeplitz-matrix/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>

#### array-nesting 
[Leetcode No565](https://leetcode.com/problems/array-nesting/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>

#### max-chunks-to-make-sorted  
[Leetcode No769](https://leetcode.com/problems/max-chunks-to-make-sorted/)
<details>
  <summary>Solution</summary>
  
```python
```
</details>