### 95. Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Constraints:
    0 <= n <= 8
#### Python
```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.ways(1,n)
        
    def ways(self,start, end):
        result=[]
        if (start>end):
            return [None]
        
        for i in range(start, end+1): # number i is root
            left_Nodes=self.ways(start,i-1)
            right_Nodes=self.ways(i+1,end)
            for l_Node in left_Nodes:
                for r_Node in right_Nodes:
                    root=TreeNode(i,l_Node,r_Node)
                    result.append(root)
        return result
```
#### Csharp
```csharp
```
