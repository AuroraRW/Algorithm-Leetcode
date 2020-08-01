```python
#DFS-preorder先序
def preorder(root):
    if root != None:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


#DFS-inorder中序
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)


#DFS-postorder后序
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")
```