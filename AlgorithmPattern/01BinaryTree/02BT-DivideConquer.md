### 3. Divide Conquer

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

#### [maximum-depth-of-binary-tree No104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

> 给定一个二叉树，找出其最大深度。

思路 1：分治法

```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

思路 2：层序遍历

```Python
class Solution:
    def maxDepth(self, root: TreeNode) -> List[List[int]]:
        
        depth = 0
        if root is None:
            return depth
        
        bfs = collections.deque([root])
        
        while len(bfs) > 0:
            depth += 1
            level_size = len(bfs)
            for _ in range(level_size):
                node = bfs.popleft()
                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)
        
        return depth
```

#### [balanced-binary-tree No110](https://leetcode.com/problems/balanced-binary-tree/)

> 给定一个二叉树，判断它是否是高度平衡的二叉树。

思路 1：分治法，左边平衡 && 右边平衡 && 左右两边高度 <= 1，

```Python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
 
        def depth(root):
            
            if root is None:
                return 0, True
            
            dl, bl = depth(root.left)
            dr, br = depth(root.right)
            
            return max(dl, dr) + 1, bl and br and abs(dl - dr) < 2
        
        _, out = depth(root)
        
        return out
```

思路 2：使用后序遍历实现分治法的迭代版本

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

#### [binary-tree-maximum-path-sum No124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

> 给定一个**非空**二叉树，返回其最大路径和。

思路：分治法。最大路径的可能情况：左子树的最大路径，右子树的最大路径，或通过根结点的最大路径。其中通过根结点的最大路径值等于以左子树根结点为端点的最大路径值加以右子树根结点为端点的最大路径值再加上根结点值，这里还要考虑有负值的情况即负值路径需要丢弃不取。

```Python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.maxPath = float('-inf')
        
        def largest_path_ends_at(node):
            if node is None:
                return float('-inf')
            
            e_l = largest_path_ends_at(node.left)
            e_r = largest_path_ends_at(node.right)
            
            self.maxPath = max(self.maxPath, node.val + max(0, e_l) + max(0, e_r), e_l, e_r)
            
            return node.val + max(e_l, e_r, 0)
        
        largest_path_ends_at(root)
        return self.maxPath
```

#### [lowest-common-ancestor-of-a-binary-tree No236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

> 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

思路：分治法，有左子树的公共祖先或者有右子树的公共祖先，就返回子树的祖先，否则返回根节点

```Python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None
```