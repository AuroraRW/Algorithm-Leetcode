# Tree
## **Recursion**
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

#### diameter-of-binary-tree
[Leetcode No543](https://leetcode.com/problems/diameter-of-binary-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### invert-binary-tree
[Leetcode No226](https://leetcode.com/problems/invert-binary-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### merge-two-binary-trees
[Leetcode No671](https://leetcode.com/problems/merge-two-binary-trees/)
<details>
  <summary>Solution</summary>
  
</details>

#### path-sum
[Leetcode No112](https://leetcode.com/problems/path-sum/)
<details>
  <summary>Solution</summary>
  
</details>

#### path-sum-iii
[Leetcode No437](https://leetcode.com/problems/path-sum-iii/)
<details>
  <summary>Solution</summary>
  
</details>

#### subtree-of-another-tree
[Leetcode No572](https://leetcode.com/problems/subtree-of-another-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### symmetric-tree
[Leetcode No101](https://leetcode.com/problems/symmetric-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### minimum-depth-of-binary-tree
[Leetcode No111](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### sum-of-left-leaves
[Leetcode No404](https://leetcode.com/problems/sum-of-left-leaves/)
<details>
  <summary>Solution</summary>
  
</details>

#### longest-univalue-path
[Leetcode No687](https://leetcode.com/problems/longest-univalue-path/)
<details>
  <summary>Solution</summary>
  
</details>

#### house-robber-iii
[Leetcode No337](https://leetcode.com/problems/house-robber-iii/)
<details>
  <summary>Solution</summary>
  
</details>

#### second-minimum-node-in-a-binary-tree
[Leetcode No671](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/)
<details>
  <summary>Solution</summary>
  
</details>

## **BFS**

#### average-of-levels-in-binary-tree
[Leetcode No637](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
<details>
  <summary>Solution</summary>
  
```python
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if not root:
            return result
        # use queue to store each level
        q = []
        q.append(root)
        while len(q) != 0:
            num=len(q)
            level_v=0
            for i in range(num):
                r = q.pop(0)
                level_v+=r.val
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            result.append(level_v/num)
                    
        return result
```
</details>

#### find-bottom-left-tree-value
[Leetcode No513](https://leetcode.com/problems/find-bottom-left-tree-value/)
<details>
  <summary>Solution</summary>
  
</details>

## **BST**
#### trim-a-binary-search-tree
[Leetcode No669](https://leetcode.com/problems/trim-a-binary-search-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### kth-smallest-element-in-a-bst
[Leetcode No230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
<details>
  <summary>Solution</summary>
  
</details>

#### convert-bst-to-greater-tree
[Leetcode No538](https://leetcode.com/problems/convert-bst-to-greater-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### lowest-common-ancestor-of-a-binary-search-tree
[Leetcode No235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### convert-sorted-array-to-binary-search-tree
[Leetcode No108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### convert-sorted-list-to-binary-search-tree
[Leetcode No109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)
<details>
  <summary>Solution</summary>
  
</details>

#### two-sum-iv-input-is-a-bst
[Leetcode No653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
<details>
  <summary>Solution</summary>
  
</details>

#### minimum-absolute-difference-in-bst
[Leetcode No530](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
<details>
  <summary>Solution</summary>
  
</details>

#### find-mode-in-binary-search-tree
[Leetcode No501](https://leetcode.com/problems/find-mode-in-binary-search-tree/)
<details>
  <summary>Solution</summary>
  
</details>