## **Binary Search Tree-BST**

#### validate-binary-search-tree 
[Leetcode No98](https://leetcode.com/problems/validate-binary-search-tree/)
<details>
  <summary>Solution - Inorder Traversal</summary>

Inorder traversal, then check
```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        def inorder(root):
            if root is None:
                return root
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        for i in range(1,len(result)):
            if result[i]<=result[i-1]:
                return False
        return True
```
</details>

<details>
  <summary>Solution - Divide Conquer</summary>
From up to bottom, check if the current node is in the right interval

```Python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def Valid(root, min_v, max_v):
            if root is None:
                return True
            if (root.val<=min_v) or (root.val>=max_v):
                return False
        
            return Valid(root.left, min_v, root.val)and Valid(root.right, root.val, max_v)
        
        if root==None:
            return True
        
        return Valid(root.left, float('-inf'), root.val) and Valid(root.right, root.val, float('inf'))
```
</details>

<details>
  <summary>Solution - Intervative</summary>
??????
思路 3：利用二叉搜索树的性质，根结点为左子树的右边界，右子树的左边界，使用先序遍历自顶向下更新左右子树的边界并检查是否合法，迭代版本实现简单且可以提前返回结果。

```Python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        s = [(root, float('-inf'), float('inf'))]
        while len(s) > 0:
            node, low, up = s.pop()
            if node.left is not None:
                if node.left.val <= low or node.left.val >= node.val:
                    return False
                s.append((node.left, low, node.val))
            if node.right is not None:
                if node.right.val <= node.val or node.right.val >= up:
                    return False
                s.append((node.right, node.val, up))
        return True
```
</details>

#### insert-into-a-binary-search-tree 
[Leetcode No701](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
<details>
  <summary>Solution</summary>

> 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。

思路：如果只是为了完成任务则找到最后一个叶子节点满足插入条件即可。但此题深挖可以涉及到如何插入并维持平衡二叉搜索树的问题，并不适合初学者。

```Python
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return TreeNode(val)
        
        node = root
        while True:
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
```
</details>