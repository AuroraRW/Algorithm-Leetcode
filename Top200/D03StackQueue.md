# Satck and Queue

#### implement-queue-using-stacks 
[Leetcode No232](https://leetcode.com/problems/implement-queue-using-stacks/)
<details>
  <summary>Solution</summary>

  ```python
  # use Last In First Out to implement First In First Out
  class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[]
        self.s2=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2 !=[]:
            return self.s2.pop()
        else:
            while self.s1!=[]:
                temp=self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
            
    #just get the element, not remove
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2 !=[]:
            return self.s2[-1]
        else:
            while self.s1!=[]:
                temp=self.s1.pop()
                self.s2.append(temp)
            return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1==[] and self.s2==[]
  ```
</details>

#### implement-stack-using-queues 
[Leetcode No225](https://leetcode.com/problems/implement-stack-using-queues/)
<details>
  <summary>Solution</summary>

  ```python
  # use First In First Out to implement Last In First Out
  # insert from front, so the queue turn into stack
  # in order to insert from front, we append it then convert the queue 
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for i in range (len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q
  ```
</details>

#### min-stack 
[Leetcode No155](https://leetcode.com/problems/min-stack/)
<details>
  <summary>Solution</summary>
  Two stack, one is data, the other is min vlaue. Both of them update at the same time

  ```python
  class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataStack=[]
        self.minStack=[]
        self.minimum=float('inf')

    def push(self, x: int) -> None:
        self.dataStack.append(x)
        self.minimum=min(self.minimum, x)
        self.minStack.append(self.minimum)
        
    def pop(self) -> None:
        self.dataStack.pop()
        self.minStack.pop()
        if not self.minStack:
            self.minimum=float('inf')
        else:
            self.minimum=self.minStack[-1]
        
    def top(self) -> int:
        return self.dataStack[-1]     

    def getMin(self) -> int:
        return self.minStack[-1]
  ```
</details>

#### valid-parentheses 
[Leetcode No20](https://leetcode.com/problems/valid-parentheses/)
<details>
  <summary>Solution</summary>

  ```python
  class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in ['(','[','{']:
                    stack.append(c)
                else:
                    t=stack.pop()
                    if (t=='(' and c!=')') or (t=='[' and c!=']') or (t=='{' and c!='}'):
                        return False
        return not stack
  ```
</details>

#### daily-temperatures 
[Leetcode No739](https://leetcode.com/problems/daily-temperatures/)
<details>
  <summary>Solution</summary>

  Ref:https://www.youtube.com/watch?v=d4FvlTzzWjQ
  ```python
  class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # the element of this stack is (temperatures, index)
        result=[0]*len(T)
        stack=[]
        for i,v in enumerate(T):
            while stack and stack[-1][0]<v:
                index=stack[-1][1]
                result[index]=i-index
                stack.pop()
            stack.append((v,i))
        return result
  ```
</details>

#### next-greater-element-ii 
[Leetcode No503](https://leetcode.com/problems/next-greater-element-ii/)
<details>
  <summary>Solution</summary>

  ```python
  ```
</details>

## Summary
- Difference operations between stack and queue
