#### 53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#### Python
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
#### CSharp
```csharp
public class Solution {
    public int MaxSubArray(int[] nums) {
        if(nums==null||nums.Length==0)
            return 0;
        int presum=nums[0];
        int maxsum=presum;
        for(int i=1;i<nums.Length; i++){
            if(presum<0) presum=nums[i];
            else presum=presum+nums[i];
            maxsum=Math.Max(maxsum, presum);
        }
            
        return maxsum;
    }
}
```