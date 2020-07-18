### Sorting Algorithm
![title](#01.png)
![title](#02.png)
### 1 Bubble Sort
#### Python
```python
def BubbleSort(arry: list)->list:
    # begin from 1, total n-1 times
    for i in range(1,len(arry)):
        # begin form 0, total n-1 times
        for j in range(0,len(arry)-i):
            if arry[j]>arry[j+1]:
                arry[j], arry[j+1]=arry[j+1],arry[j]    
    return arry
```
### 2 Selection Sort
#### Python
```python
def SelectionSort(arry: list)-> list:
    for i in range(len(arry)-1):
        #m is the index of minimum 
        m=i
        for j in range(i+1,len(arry)):
            if arry[j]<arry[m]:
                m=j
        arry[m],arry[i]=arry[i],arry[m]   
    return arry
```
### 3 Insertion Sort
#### Python
```python
def InsertionSort(arry : list)-> list:
    #from the second number to insert
    for i in range(1,len(arry)):
        for j in range(i,0,-1):
            if arry[j-1]>arry[j]:
                arry[j-1],arry[j]=arry[j],arry[j-1]
                
    return arry
```
```python
def InsertionSort(arry : list)-> list:
    #from the second number to insert
    for i in range(1,len(arry)):
        #copy the number
        if arry[i-1]>arry[i]:
            temp=arry[i]
            #move backword until find the right place
            for j in range(i-1,-1,-1):
                if temp<arry[j]:
                    arry[j+1]=arry[j]
                else:
                    #insert
                    arry[j+1]=temp
                    break
                #temp is the minimum, left end
                if j==0:
                    arry[j]=temp               
    return arry
```
### 4 Shell Sort
#### Python
```python
def ShellSort(arry: List)-> List:
    gap = len(arry) // 2
    while gap >= 1:
        for j in range(gap, len(arry)):
            i = j
            while (i - gap) >= 0:
                if arry[i] < arry[i - gap]:
                    arry[i], arry[i - gap] = arry[i - gap], arry[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return arry
```
### 5 Merge Sort
#### Python
```python
def MergeSort(arry:list,left:int, right:int):
    if left<right:
        center=(left+right)//2
        MergeSort(arry,left,center)
        MergeSort(arry,center+1,right)
        Merge(arry,left,center,right)
    return
def Merge(arry:list,left:int, center:int, right:int):
    i=left
    j=center+1
    temp=[]
    while i<=center and j<=right:
        if arry[i]<arry[j]:
            temp.append(arry[i])
            i+=1
        else:
            temp.append(arry[j])
            j+=1
    if i<=center:
        for t in range(i,center+1):
            temp.append(arry[t])
    if j<=right:
        for t in range(j,right+1):
            temp.append(arry[t])
    for t in range(left,right+1):
        arry[t]=temp[t-left]
```
### 6 Quick Sort
#### Python
```python
def partition(arry:list, left:int, right:int )->int:
    i=left+1
    j=right
    while i<j:
        while i<=j and arry[i]<=arry[left]:
            i+=1
        while i<=j and arry[j]>=arry[left]:
            j-=1
            
        #exchange
        if i<j:
            arry[i],arry[j]=arry[j],arry[i]
    #exchange pivot to j, not i
    arry[left],arry[i]=arry[i],arry[left]
    
    return j

def QuickSort(arry:list, left:int, right:int):
    if left<right:
        center=partition(arry,left,right)
        QuickSort(arry,left,center-1)
        QuickSort(arry,center+1,right)
```

#### Reference
https://www.runoob.com/w3cnote/ten-sorting-algorithm.html