"""
Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.xLevel=-1
        self.yLevel=-1
        self.xParent=None
        self.yParent=None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        #we do not need to create tree in leetcode
        def add(arr, root, i, n):
            if i < n:
                root = TreeNode(arr[i])
                # insert left child
                root.left = add(arr, root.left, 2 * i + 1, n)
                # insert right child
                root.right = add(arr, root.right, 2 * i + 2, n)
            return root
        def dfs(root, x, y, level, parent):
            if root == None:
                return
            if root.val == x:
                xLevel = level
                xParent = parent
            if root.val == y:
                yLevel = level
                yParent = parent
            if (root.left != None):
                dfs(root.left, x, y, level+1, root.val)
            if (root.right != None):
                dfs(root.right, x, y, level+1, root.val)

        r = add(root, None, 0, len(root))
        dfs(r, x, y, 1, None)
        if self.xLevel==self.yLevel and self.xParent != self.yParent:
            return True
        else:
            return False


if __name__=="__main__":
    S=Solution()
    print(S.isCousins([1,2,3,None,4,None,5], 5, 4))
