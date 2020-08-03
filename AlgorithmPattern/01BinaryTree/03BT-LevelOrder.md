### BFS 层次应用

#### [binary-tree-zigzag-level-order-traversal No103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

> 给定一个二叉树，返回其节点值的锯齿形层次遍历。Z 字形遍历

思路：在BFS迭代模板上改用双端队列控制输出顺序

```Python
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        levels = []
        if root is None:
            return levels
        
        s = collections.deque([root])

        start_from_left = True
        while len(s) > 0:
            levels.append([])
            level_size = len(s)
            
            if start_from_left:
                for _ in range(level_size):
                    node = s.popleft()
                    levels[-1].append(node.val)
                    if node.left is not None:
                        s.append(node.left)
                    if node.right is not None:
                        s.append(node.right)
            else:
                for _ in range(level_size):
                    node = s.pop()
                    levels[-1].append(node.val)
                    if node.right is not None:
                        s.appendleft(node.right)
                    if node.left is not None:
                        s.appendleft(node.left)
            
            start_from_left = not start_from_left
            
        
        return levels
```