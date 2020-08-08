## **Recursion Questions**
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