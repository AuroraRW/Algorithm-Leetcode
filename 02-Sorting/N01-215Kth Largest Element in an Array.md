### 215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
#### Python
Sort  
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True) #from big to small
        return nums[k-1]
```
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        r=sorted(nums)  #from small to big
        return r[len(nums)-k]
```
Heap  

#### Charp
```csharp
public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        Array.Sort(nums);
        return nums[nums.Length - k];
    }
}
```
HeapSort  
```csharp
public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        heapSort(nums);
        return nums[nums.Length-k];
    }
    private void swap(int[] tree, int i, int j)
    {
        int temp = tree[i];
        tree[i] = tree[j];
        tree[j] = temp;
    }
    private void heapify(int[] tree, int n, int i)
    {
        int c1 = 2 * i + 1;
        int c2 = 2 * i + 2;
        int max = i;
        //int n = tree.Length;
        if (i >= n) return;
        
        if (c1<n && tree[c1] > tree[max])
        {
            max = c1;
        }
        if(c2<n && tree[c2] > tree[max])
        {
            max = c2;
        }
        if (max != i)
        {
            swap(tree, i, max);

            heapify(tree, n, max);
        }
    }
    private void buildMaxHeap(int[] tree, int n)
    {
        //int n = tree.Length;
        int last_node = n - 1;
        int parent = (last_node - 1) / 2;
        for (int i=parent; i>=0; i--)
        {
            heapify(tree, n, i);
        }
    }
    private void heapSort(int[] tree)
    {
        int n = tree.Length;
        buildMaxHeap(tree, n);
        for (int i = n - 1; i >= 0; i--)
        {
            swap(tree, i, 0);
            heapify(tree, i, 0);
        }
    }
}
```