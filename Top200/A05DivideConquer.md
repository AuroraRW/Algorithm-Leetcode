# Divide Conquer

#### different-ways-to-add-parentheses 
[Leetcode No241](https://leetcode.com/problems/different-ways-to-add-parentheses/)
<details>
  <summary>Solution</summary>

```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        result=[]
        for i in range(len(input)):
            if input[i] in {'+','-','*'}:
                left=self.diffWaysToCompute(input[0:i])
                right=self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i]=='+':
                            result.append(l+r)
                        if input[i]=='-':
                            result.append(l-r)
                        if input[i]=='*':
                            result.append(l*r)
                
        if len(result)==0:
            result.append(int(input))
        result.sort()
        return result
```
```python
class Solution:
    def diffWaysToCompute(self, input):    
        ops = {'+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y}
        def ways(s):
            ans = []
            for i in range(len(s)):
                if s[i] in "+-*":          
                    ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
            if not ans: ans.append(int(s))
            return ans
    
        return ways(input)
```
</details>

#### unique-binary-search-trees-ii 
[Leetcode No95](https://leetcode.com/problems/unique-binary-search-trees-ii/)

<details>
  <summary>Solution</summary>

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
<details>