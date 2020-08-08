## **Divide and Conquer**

先分别处理局部，再合并结果

适用场景

- 快速排序
- 归并排序
- 二叉树相关问题

分治法模板

- 递归返回条件
- 分段处理
- 合并结果

常见题目示例

#### maximum-depth-of-binary-tree 
[Leetcode No104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
<details>
  <summary>Solution</summary>

1. Divide Conquer
```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
2. Level Order
```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        result = 0
        if not root:
            return result
        # use queue
        q = []
        q.append(root)
        while len(q) != 0:
            result=result+1
            for i in range(len(q)):
                r = q.pop(0)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)

        return result
```
</details>

#### balanced-binary-tree 
[Leetcode No110](https://leetcode.com/problems/balanced-binary-tree/)
<details>
  <summary>Solution</summary>

a height-balanced binary tree:  
a binary tree in which the left and right subtrees of **every** node differ in height by no more than 1.

1. 分治法，左边平衡 && 右边平衡 && 左右两边高度 <= 1，

```Python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
    
        d, result= self.depth(root)
        return result
        
    def depth(self, root):
        
        if root is None:
            return 0, True

        depth_left, res_left=self.depth(root.left)
        depth_right, res_right=self.depth(root.right)
        
        dep=max(depth_left, depth_right)+1 
        result=res_left and res_right and abs(depth_left-depth_right)<2
        
        return dep, result
```

2. Interative-posorder??

```Python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        s = [[TreeNode(), -1, -1]]
        node, last = root, None
        while len(s) > 1 or node is not None:
            if node is not None:
                s.append([node, -1, -1])
                node = node.left
                if node is None:
                    s[-1][1] = 0
            else:
                peek = s[-1][0]
                if peek.right is not None and last != peek.right:
                    node = peek.right
                else:
                    if peek.right is None:
                        s[-1][2] = 0
                    last, dl, dr = s.pop()
                    if abs(dl - dr) > 1:
                        return False
                    d = max(dl, dr) + 1
                    if s[-1][1] == -1:
                        s[-1][1] = d
                    else:
                        s[-1][2] = d
        
        return True
```
</details>

#### binary-tree-maximum-path-sum 
[Leetcode No124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
<details>
  <summary>Solution</summary>

Given a non-empty binary tree, find the maximum path sum.
Four ways:  
1. current node + left subtree
2. current node + right subtree
3. current node
4. current node + left subtree + right subtree

```Python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result=float('-inf')
        
        def Submax(root):
            if root is None:
                return 0
            left=max(0, Submax(root.left))
            right=max(0, Submax(root.right))
            self.result=max(self.result, left+right+root.val)

            return max(left, right)+root.val
        
        Submax(root)
        
        return self.result
```
</details>

#### lowest-common-ancestor-of-a-binary-tree 
[Leetcode No236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
<details>
  <summary>Solution</summary>

```Python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # return condition
        if root is None:
            return None
        # return condition: if meet p or q, then stop
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # find both
        if left is not None and right is not None:
            return root
        # find one
        elif left is not None:
            return left
        elif right is not None:
            return right
        # find noting 
        else:
            return None
```
</details>

## **Summary**
- **Difference between Divide Conquer and Recursive Traversal:**  
*Divide Conquer*:   divide, merge  
*Recursive Traversal*:  need global variable